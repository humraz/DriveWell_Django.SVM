from rest_framework import serializers
from snipetss.models import Snippet
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('title', 'code')