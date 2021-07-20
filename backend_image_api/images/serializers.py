
# The serializer can be defined explicitly using django rest framework renderers

# However, for a standard use-case(standard json response stuff),  you
# can just use the pre-written serializers from the framework

from rest_framework import serializers

from .models import ImageModel


# Here, the ModelSerializer is one of the default serializers in DRF for a REST API
# It will show all the fields of the model in the response and it also allows to
# create new objects in the model and update the object in the model 
# It will also give appropriate response based on the client automatically
# For instance, if the request is being made from a web browser, it will return a 
# automatically rendered HTML response. But, for other usecases(eg: Postman), it will
# simply return the json. 
class ImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = ('id','category','title','image','created','author')
