from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, ImageForm
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    context = {'images_list':images_list}
    #return render(request, 'gallery/index.html', context)
    #Serialize as json
    return HttpResponse(serializers.serialize("json", images_list))


#If you want to read from FORM model use this method
#def add_image(request):
#    if request.method == 'POST':
#        form = ImageForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('index'))
#    else:
#        form = ImageForm()
#
#    return render(request, 'gallery/image_form.html', {'form': form})

@csrf_exempt
def add_image(request):
    if request.method == 'POST':
        new_image = Image(
            name=request.POST.get('name'),
            url=request.POST.get('url'),
            description=request.POST.get('description'),
            imageFile=request.FILES['imageFile'],
        )
        new_image.save()
        return HttpResponse(serializers.serialize("json", [new_image]))


def view_images(request):
    return render(request, "gallery/index.html")


def add_images_view(request):
    return render(request, "gallery/image_form.html")
