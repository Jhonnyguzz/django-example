from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Image, ImageForm

# Create your views here.
def index(request):
    images_list = Image.objects.all()
    context = {'images_list':images_list}
    return render(request, 'gallery/index.html', context)


def add_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ImageForm()

    return render(request, 'gallery/image_form.html', {'form': form})

