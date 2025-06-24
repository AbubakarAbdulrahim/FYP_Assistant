from rest_framework import serializers
from .models import Reference

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'project', 'style', 'citation_text', 'source_url', 'added_manually', 'created_at']
        read_only_fields = ['id', 'added_manually', 'created_at']
