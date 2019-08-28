import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .models import Image, ImageForm

# Create your views here.
@csrf_exempt
def index(request):
    images_list = Image.objects.all()
    context = {'images_list':images_list}
    #return render(request, 'gallery/index.html', context)
    #Serialize as json
    val = request.user.is_authenticated
    if val:
        images_list = Image.objects.filter(user=request.user)
    else:
        images_list = Image.objects.all()
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
            user=request.user
        )
        new_image.save()
        return HttpResponse(serializers.serialize("json", [new_image]))


@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.save()
    return HttpResponse(serializers.serialize("json", [user_model]))


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = "ok"
        else:
            message = 'Nombre de usuario o contraseña incorrectos'

    return JsonResponse({"message": message})


@csrf_exempt
def is_user_auth(request):
    if request.user.is_authenticated:
        message = 'yes'
    else:
        message = 'no'

    return JsonResponse({"message": message})


@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"message":'ok'})


def view_images(request):
    return render(request, "gallery/index.html")


def add_images_view(request):
    return render(request, "gallery/image_form.html")


def add_user_view(request):
    return render(request, "gallery/register.html")


def login_user(request):
    return render(request, "gallery/login.html")
