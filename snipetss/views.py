from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from snipetss.models import Snippet, Flag
from rest_framework.decorators import api_view
from snipetss.serializers import SnippetSerializer
from snipetss.serializers import MyPhotoSerializer,MyFlagSerializer
from rest_framework.views import APIView
from django.shortcuts import render
from django.utils import timezone
from BatchProcessor import ClassifyAndScore
from django.db.models import Sum,Avg

class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FlagList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    
    def post(self, request, format=None):
        serializer = MyFlagSerializer(data=request.data)
	
	nu=request.data.get('score')
	print nu
	if nu == '1':
		sc=ClassifyAndScore()
		print sc 
		sav= Snippet.objects.create(drivername= 'krishnan', score= sc)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def post_list(request):
	posts = Snippet.objects.order_by().values('drivername').distinct() 
	return render(request, 'index2.html', {'posts': posts})



class PhotoList(APIView):
    def post(self, request, format=None):
        serializer = MyPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def ListDrivertrips(request, driver_name):
    drivertrips = Snippet.objects.filter(drivername=driver_name)
    cumscore = Snippet.objects.filter(drivername=driver_name).aggregate(Avg('score'))['score__avg']
    context = {
        'drivertrips': drivertrips,
        'driver_name': driver_name,
        'cumscore': cumscore,
    }
    return render(request, 'trips.html', context)

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
