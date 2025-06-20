from rest_framework import serializers
from .models import FeedbackUpload, FeedbackItem
from project.models import Chapter

# feedback upload serializer
class FeedbackUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackUpload
        fields = ['id', 'project', 'file', 'uploaded_at', 'processed']

# feedback item serializer
class FeedbackItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackItem
        fields = ['id', 'chapter', 'page_number', 'comment_text', 'position', 'resolved', 'created_at']

# assign chapter -> feedback serializer
class AssignFeedbackChapterSerializer(serializers.Serializer):
    chapter_id = serializers.IntegerField()

    def validate_chapter_id(self, value):
        try:
            chapter = Chapter.objects.get(id=value)
        except Chapter.DoesNotExist:
            raise serializers.ValidationError("Chapter does not exist.")
        return chapter

    def update(self, instance, validated_data):
        instance.chapter = validated_data['chapter_id']
        instance.save()
        return instance