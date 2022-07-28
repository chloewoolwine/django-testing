from django.shortcuts import render
from django.http import HttpResponse
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

"""
students = [
    {
        'name':'Count Dracula',
        'id':'cd1',
        'stat':"vampire",
        'stat2': 20000
    },
    {
        'name':'Jonathan Harker',
        'id':'jhh2132',
        'stat':"profesional victim",
        'stat2': 4
    }
]"""

def home(request):
    #todo: unique number identification for classes
    students_data = database.child('class').child('students').get()
    students = []
    for student_data in students_data.each():
        print(student_data.key())
        students.append(student_data.val())
        #single_student = {}
        #for data in student_data.val():
            #single_student[data.key()] = data.val()

    context = {
        'students' : students
    }
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html', {'title':'about'})
