"""
URL configuration for velleearning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from development import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('',views.loadhomepage,name="index.html"),
     path("homelink",views.loadhomepage),
     path("aboutus",views.loadaboutuspage),
     path("contactus",views.loadcontactuspage),
     path("feedback",views.loadfeedbackpage),
     path("loginlink",views.loadloginpage),
     path("signuplink",views.loadsignuppage),
     path("logoutlink",views.loadlogoutpage),
     path("jobslink",views.loadjobspage),
     path("userdeletelink",views.loaddeleteuser),
     path("jobdeletelink",views.loadjobdeleteaction),
     path("feedbacklink",views.loadfeedbackpage),
     path("feedbackactioncode",views.loadfeedbackaction),
     path("Jobseekerdashboardlink",views.loadJobseekerdashboard),
     path("signupcodeaction",views.loadsignupcode),
     path("logincodeaction",views.loadlogincode),
     path("logincodeaction1",views.loadlogincode1),
     path("jobsprovidelink",views.loadjobpage),
     path("jobcodeaction",views.loadjobs),
     path("Userdeleteaction",views.loaduserdeletecode),
     path("Jobseekerpasswordchangelink",views.loadJobseekerpasschange),
     path("passchangecodeaction",views.loadpasschangecode),
     path("Jobproviderpasswordchangelink",views.loadJobproviderpasschange),
     path("passchangecodeaction1",views.loadpasschangecode1),
     path("displayfeedbacklink",views.loadfeedback),
]
