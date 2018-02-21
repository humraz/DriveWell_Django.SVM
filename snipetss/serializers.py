from rest_framework import serializers
from snipetss.models import Snippet
from snipetss.models import MyPhoto
from snipetss.models import Flag
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet	
        fields = ('drivername','timecreated','date','score')

class MyPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPhoto
        fields = ( 'name', 'image')

class MyFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = ( 'score',)
