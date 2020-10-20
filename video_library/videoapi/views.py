from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Video, Rating
from .serializers import VideoSerializer,RatingSerializer,UserSerializer
from rest_framework.response import Response

# Create your views here.
class VideoViewSet(viewsets.ModelViewSet):
  queryset= Video.objects.all()
  serializer_class = VideoSerializer
  permission_classes = (AllowAny,)

 class RatingViewSet(viewsets.ModelViewSet):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer
  permission_classes = (IsAuthenticated, )
  def delete(self,request,*args,**kwargs):
    response = {'message':'Rating cannot be updated like this'}
    return Response(response, status = status.HTTP_400_BAD_REQUEST)
