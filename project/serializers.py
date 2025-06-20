from rest_framework import serializers
from .models import Project, Chapter
from feedback.models import FeedbackItem, FeedbackUpload

# feedback upload serializer
class FeedbackUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackUpload
        fields = ['id', 'file', 'uploaded_at', 'processed']

# feedback item serializer
class FeedbackItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackItem
        fields = ['id', 'chapter', 'page_number', 'comment_text', 'position', 'resolved', 'created_at']


#
#
#


# project list serilizer
class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'status', 'created_at']

# project detail serializer
class ProjectDetailSerializer(serializers.ModelSerializer):
    feedback_uploads = FeedbackUploadSerializer(many=True, read_only=True)
    feedback_items = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'last_modified']

    def get_feedback_items(self, obj):
        feedbacks = FeedbackItem.objects.filter(chapter__project=obj)
        return FeedbackItemSerializer(feedbacks, many=True).data

# project update serializer
class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'abstract', 'field']
