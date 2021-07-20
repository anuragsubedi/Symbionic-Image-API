# Even for the views, you can either create the views explicitly or you can take some shortcuts
# by just inheriting stuff from the DRF. The viewsets.ModelViewset is going to take care of all 
# the views i.e. (get, post, etc requests)

from django.shortcuts import render
from rest_framework import viewsets

from .models import ImageModel
from .serializers import ImageModelSerializer

# So, instead of defining explicit methods for each view endpoint(get, post, put, etc), you can 
# directly use the ModelViewSet class of the viewsets module

class ImageModelView(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()         # The ModelViewSet will figure out how to use particular objects in a particular way from the queryset table
    serializer_class = ImageModelSerializer 
