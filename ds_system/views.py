from pyexpat.errors import messages
from django.conf import UserSettingsHolder
from django.shortcuts import redirect, render
from grpc import AuthMetadataContext

from dsinventory.settings import AUTH_PASSWORD_VALIDATORS

# Create your views here.

def index(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = AuthMetadataContext.authenticate(username = username, password =password  )

        if user is not None:
            AUTH_PASSWORD_VALIDATORS.login(request , user)
            return redirect('/home')    
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/")
    else:
        return render(request,'index.html')

def register(request):

    if request.method == 'POST':

        email = request.POST['email']
        username = request.POST['username']
        password= request.POST['password']


        user = UserSettingsHolder.objects.create_user(username = username , password = password , email = email)
        user.save()
        print('user created')
        return redirect('/custom')

    return render(request,'register.html')


def custom(request):
    return render(request, 'custom.html')


def home(request):
    return render(request, 'home.html')
