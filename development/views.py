import sqlite3
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from unicodedata import category



# Create your views here.

def loadhomepage(request):
    return render(request,'index.html')
def loadaboutuspage(request):
    return render(request,'aboutus.html')
def loadcontactuspage(request):
    return render(request, 'contactus.html')
def loadfeedbackpage(request):
    return render(request, 'feedback.html')
def loadloginpage(request):
    return render(request, 'login.html')

def loadfeedbackpage(request):
    return render(request, 'feedback.html')

def loadsignuppage(request):
    return render(request, 'signup.html')
def loaddeleteuser(request):
    return render(request,"Userdelete.html")
def loadjobs(request):
    return render(request,"Jobproviderdashboard.html ")

def loadlogoutpage(request):
    return render(request, 'index.html')

def loadjobpage(request):
    return render(request, 'Job.html')
def loadJobseekerpasschange(request):
    return render(request, 'Jobseekerpasswordchange.html')
def loadJobproviderpasschange(request):
    return render(request,'Jobproviderpasschange.html')
def loadjobspage(request):
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql = "select * from jobtable"
    result = operation.execute(sql)
    records = result.fetchall()
    return render(request,'viewalljobs.html',{'list':records})


def loadjobs(request):
    JobID = request.POST['jobid']
    JobName  = request.POST['name']
    Jobstyle = request.POST['type']
    Amount = request.POST['amount']
    Jobspecification = request.POST['specific']
    Status = request.POST['status']
    Duration = request.POST['duration']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql = "insert into jobtable values(?,?,?,?,?,?,?)"
    values = (JobID, JobName, Jobstyle, Amount, Jobspecification, Status, Duration)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, 'Job.html')



def loadJobseekerdashboard(request):
    return render(request, 'jobseekerdashboard.html')


def loadlogincode(request):
    UserId = request.POST['id']
    Password = request.POST['password']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql = "select * from JobproviderSignUptable where ProviderId = ? and Password = ?"
    values = (UserId, Password)
    result = operation.execute(sql, values)

    if (result.fetchone()):
        return render(request, 'Jobproviderdashboard.html')
    else:
        return render(request, 'login.html', {'message1': "invalid id/password"})


def loadlogincode1(request):
        UserId = request.POST['id']
        Password = request.POST['password']
        con = sqlite3.connect('db.sqlite3');
        operation = con.cursor()
        sql = "select * from jobseekersignuptable where seekerId = ? and Password = ?"
        values = (UserId, Password)
        result = operation.execute(sql, values)

        if (result.fetchone()):
            return render(request, 'Jobseekerdashboard.html')
        else:
            return render(request, 'login.html',{'message1':"invalid id/password"})


def loadsignupcode(request):
        UserId = request.POST['id']
        Password = request.POST['password']
        Fullname = request.POST['fullname']
        Age = request.POST['age']
        PermanentAddress = request.POST['address']
        contactNumber = request.POST['contact']
        DOB = request.POST['date']
        category = request.POST['category']
        Email = request.POST['email']
        Subscription = request.POST['subscribe']
        Education = request.POST['education']
        skills = request.POST['skills']
        con = sqlite3.connect('db.sqlite3');
        operation = con.cursor()
        if category == "Job Seeker":
            sql = "insert into jobseekersignuptable values(?,?,?,?,?,?,?,?,?,?,?)"
            values = ( UserId, Password, Fullname, PermanentAddress, contactNumber, DOB, Education, Email, Subscription, skills,
            Age)
            operation.execute(sql, values)
            con.commit()
            con.close()
            return render(request, 'login.html')
        elif category == "Job Provider":
            sql = "insert into JobproviderSignUptable values(?,?,?,?,?,?,?,?,?,?,?)"
            values = (UserId, Password, Fullname, PermanentAddress, contactNumber, DOB, Email, Subscription, Education, skills,
            Age)
            operation.execute(sql, values)
            con.commit()
            con.close()
            return render(request, 'login.html')

def loadpasschangecode(request):
    ID = request.POST['id']
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql="select * from Jobseekersignuptable where SeekerId = ? AND Password = ?"
    values = (ID,oldpassword)
    result=operation.execute(sql,values)
    if(result.fetchone()):
        sql1="update Jobseekersignuptable set Password = ? where SeekerId = ?"
        values1 = (newpassword,ID)
        operation.execute(sql1,values1)
        con.commit()
        con.close()
        return render(request, 'login.html')
    else:
        return render(request, 'Jobseekerpasswordchange.html')

def loadpasschangecode1(request):
    ID = request.POST['id']
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql="select * from Jobprovidersignuptable where ProviderId = ? AND Password = ?"
    values = (ID,oldpassword)
    result=operation.execute(sql,values)
    if(result.fetchone()):
        sql1="update Jobprovidersignuptable set Password = ? where ProviderId = ?"
        values1 = (newpassword,ID)
        operation.execute(sql1,values1)
        con.commit()
        con.close()
        return render(request, 'login.html')
    else:
        return render(request, 'Jobproviderpasschange.html')
def loaduserdeletecode(request):
    ID = request.POST['id']
    Password = request.POST['password']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql= "select * from Jobseekersignuptable where SeekerId = ? AND Password = ?"
    values = (ID,Password)
    result=operation.execute(sql,values)
    if(result.fetchone()):
        sql1="delete from Jobseekersignuptable where SeekerId = ?"
        values1 = (ID,Password)
        operation.execute(sql1,values1)
        con.commit()
        con.close()
        return render(request, 'index.html')
    else:
        return render(request, 'Userdelete.html')

def loadfeedbackaction(request):
    Fullname = request.POST['fullname']
    contact = request.POST['contact']
    Feedback = request.POST['feedback']
    category = request.POST['category']
    date = datetime.datetime.now()
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql = "insert into feedbacktable(Fullname,ContactNo,Feedback,datetime,categary) values(?,?,?,?,?)"
    values = (Fullname,contact,Feedback,category,date)
    operation.execute(sql, values)
    con.commit()
    con.close()
    return render(request, 'feedback.html')

def loadjobdeleteaction(request):
    JobId = request.POST['jobid']
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql = "select * from Jobtable where Jobid = ?"
    values = (JobId)
    result = operation.execute(sql, values)
    if (result.fetchone()):
        sql1 = "delete from Jobtable where JobId = ?"
        values1 = (JobId)
        operation.execute(sql1, values1)
        con.commit()
        con.close()
        return render(request, 'Jobproviderdashboard.html')
    else:
        return render(request, 'Userdelete.html')

def loadfeedback(request):
    con = sqlite3.connect('db.sqlite3');
    operation = con.cursor()
    sql = "select * from feedbacktable"
    result = operation.execute(sql)
    records = result.fetchall()
    return render(request,'viewallfeedback.html',{'list1':records})
