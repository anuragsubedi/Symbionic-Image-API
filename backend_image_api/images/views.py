# Even for the views, you can either create the views explicitly or you can take some shortcuts
# by just inheriting stuff from the DRF. The viewsets.ModelViewset is going to take care of all 
# the views i.e. (get, post, etc requests)

from django.shortcuts import render
from rest_framework import viewsets

from .models import ImageModel
from .serializers import ImageModelSerializer 

from django.views.generic import ListView

import requests 

# So, instead of defining explicit methods for each view endpoint(get, post, put, etc), you can 
# directly use the ModelViewSet class of the viewsets module

class ImageModelView(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()         # The ModelViewSet will figure out how to use particular objects in a particular way from the queryset table
    serializer_class = ImageModelSerializer 


# Now, for rendering all the images and their information from the database to a HTML file, we need another 
# function based view that fetches the json object of the list of all the entries in the database and passes
# that json as a context dictionary to the front-end.

def AllImagesView(request):
    response = requests.get('http://127.0.0.1:8000/images/')
    data = response.json()
    print(type(data))
    return render(request, 'images/all_images.html', {'data':data, 'default':requests.get('http://127.0.0.1:8000/images/1').json()})

