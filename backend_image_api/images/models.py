from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image, ImageDraw, ImageFont
from django.core.files import File
from io import BytesIO
import os




def write_symbionic(image):
    """Edits the user uploaded image """
    im = Image.open(image)
    im.convert('RGB') # convert mode
    thumb_io = BytesIO() # create a BytesIO object
    draw = ImageDraw.Draw(im)
    
    textsize = 52
    ft = ImageFont.truetype("/Users/anuragsubedi/Library/Fonts/Lato-Heavy.ttf", textsize)

    draw.text((20, 150), 'Symbionic image API', fill='green', font=ft)
    im.save(thumb_io, 'JPEG', quality=85) # save image to BytesIO object
    edited_image = File(thumb_io, name=image.name) # create a django friendly File object
    return edited_image

def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename) 


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self): 
        return self.name

class ImageModel(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=50)

    image = models.ImageField(
        upload_to='images/', default='posts/default.jpg', max_length=255
    )

    created = models.DateTimeField(default=timezone.now)
    
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')


    def save(self, *args, **kwargs):
        self.image = write_symbionic(self.image)

        super().save(*args, **kwargs)

    def __str__(self): 
        return self.title
