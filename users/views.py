from django.shortcuts import render
from django.http import HttpResponse
import pyrebase

# Your web app's Firebase configuration
firebaseConfig = {
  "apiKey": "AIzaSyAXtfmfQ79tCe7bp-lFLOGOU8Fo4GB8CeM",
  "authDomain": "django-integration-test.firebaseapp.com",
  "databaseURL": "https://django-integration-test-default-rtdb.firebaseio.com",
  "projectId": "django-integration-test",
  "storageBucket": "django-integration-test.appspot.com",
  "messagingSenderId": "278016222190",
  "appId": "1:278016222190:web:c35d145b172ccb696da4ff"
}

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

def logIn(request):
    return render(request, 'users/login.html')

def postLogIn(request):
    email = request.POST.get('email')
    pasw = request.POST.get('pass')
    print(email)

    return render(request, 'pages/home.html')