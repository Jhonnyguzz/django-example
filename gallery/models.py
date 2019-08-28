from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=1000, null=True)
    imageFile = models.ImageField(upload_to='images', null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Image is: ' + self.name + self.url


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'url', 'description', 'imageFile']
