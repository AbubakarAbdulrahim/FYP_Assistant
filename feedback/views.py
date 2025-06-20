from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import FeedbackUpload, FeedbackItem
from project.models import Project
from .services.docx_parser import extract_docx_comments, extract_pdf_comments
from .serializers import AssignFeedbackChapterSerializer


# feedback upload view
class UploadFeedbackView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    def post(self, request, project_id):
        project = Project.objects.filter(id=project_id, user=request.user).first()
        if not project:
            return Response({"detail": "Project not found or unauthorized."}, status=404)
        
        file = request.data.get('file')
        if not file:
            return Response({"detail": "No file uploaded."}, status=400)

        # save uploaded file
        upload = FeedbackUpload.objects.create(project=project, file=file)

        # extract comments
        file_path = upload.file.path
        if file.name.endswith(".docx"):
            comments = extract_docx_comments(file_path)
        elif file.name.endswith(".pdf"):
            comments = extract_pdf_comments(file_path)
        else:
            return Response({"detail": "Unsupported file type"}, status=400)

        # save feedback items
        for comment in comments:
            FeedbackItem.objects.create(
                chapter=None,
                page_number=comment.get('page'),
                comment_text=comment.get('text'),
                position=comment.get('position', ''),
                resolved=False
            )

        return Response({"comments": comments}, status=201)

# assign chapter -> feedback
class AssignChapterToFeedbackView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            feedback = FeedbackItem.objects.get(id=pk)
        except FeedbackItem.DoesNotExist:
            return Response({"detail": "Feedback not found."}, status=404)

        serializer = AssignFeedbackChapterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update(feedback, serializer.validated_data)
            return Response({"detail": "Chapter assigned successfully."})
        return Response(serializer.errors, status=400)