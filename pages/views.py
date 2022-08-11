from django.shortcuts import render
from django.http import HttpResponseRedirect
import pyrebase
# Create your views here.
#def homePageView(request):
#    return HttpResponse("hello world <3")


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

def home(request):
    #if user is logged in-> redirect to classroom page
    if('uid' in request.session):
        uid = request.session['uid']
        print(uid)
        return  HttpResponseRedirect('/class')
    #if user is not logged in-> display login buttons
    #todo: unique number identification for classes
    return render(request, 'pages/home.html', {})

def classview(request):
    students_data = database.child('class').child('students').get()
    students = []
    for student_data in students_data.each():
        print(student_data.key())
        students.append(student_data.val())

    context = {
        'students' : students
    }
    return render(request, 'pages/classview.html', context)
