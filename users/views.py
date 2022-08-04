from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, RegisterForm, ResetPasswordForm
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

def login(request):
  if(request.method == 'POST'):
    form = LoginForm(request.POST)
    if form.is_valid():
      email = request.POST.get('username')
      pasw = request.POST.get('password')
      print(email) 
      try:
        user = authe.sign_in_with_email_and_password(email, pasw)
      except:
        message = "Invalid Credentials! D:"
        return render(request, 'users/login.html', {"message":message})
      session_id = user['idToken']
      request.session['uid'] = str(session_id)
      return HttpResponseRedirect('/') #goes to home page again
  context = {}
  context['form'] = LoginForm()
  return render(request, 'users/login.html', context)

def logout(request):
  try:
    del request.session['uid']
  except:
    pass
  context = {}
  context['form'] = LoginForm()
  return render(request, 'users/login.html', context=context)

def reset(request):
  if(request.method == 'POST'):
    email = request.POST.get('email')
    try:
        authe.send_password_reset_email(email)
        message  = "A email to reset password is successfully sent"        
        print(message)
        return HttpResponseRedirect('/')
    except:
        message  = "Something went wrong, Please check the email you provided is registered or not"
        print(message)
        return render(request, "users/reset.html", {"msg":message})
  
  context = {}
  context['form'] = ResetPasswordForm() 
  return render(request, "users/reset.html", context)

def register(request):
  if(request.method == 'POST'):
    email = request.POST.get('email')
    pasw = request.POST.get('password')
    try:
      # creating a user with the given email and password
      user=authe.create_user_with_email_and_password(email,pasw)
      uid = user['localId']
      idtoken = request.session['uid']
      print(uid)
      return render()
    except:
      context = {}
      context['form'] = RegisterForm() 
      print("email already in use, try again")
      return render(request, "users/register.html",context)
  print("loading request form")
  context = {}
  context['form'] = RegisterForm() 
  return render(request, "users/register.html",context)
