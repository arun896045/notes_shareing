from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate ,logout,login
from django.http import HttpRequest
from datetime import date


# Create your views here.
def nvigate(request):
    return render(request,'nvigate.html')

def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')


def home(request):
    return render(request,'index.html')



def login1(request):
    error=""
    if request.method=="POST":
        u=request.POST['emailId']
        p=request.POST['pwd']
        user1=authenticate(username=u,password=p)
        try:
            if user1:
                login(request,user1)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}                    
    return render(request,'login.html',d)

   



def admin(request):
    error=""
    if request.method=="POST":
        u=request.POST['uname']
        p=request.POST['pwd']
        user=authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}                    
    return render(request,'admin.html',d)



def signup1(request):
    error=""
    if request.method=="POST":
       f=request.POST["fname"]
       l=request.POST['lname'] 
       contact=request.POST['contact']
       email=request.POST['email']
       pwd=request.POST['pwd']
       branch=request.POST['branch']
       role=request.POST['role']
       try:
           user=User.objects.create_user(username=email,password=pwd,first_name=f,last_name=l)
           Signup.objects.create(user=user,contact=contact,branch=branch,role=role)
           error="no"
       except:
           error="yes"  
    d={'error':error}         
    return render(request,'signup.html',d)




def admin_home(request):
    if not request.user.is_staff:
        return redirect('admin')
    a=Notes.objects.filter(status='Accept').count()
    r=Notes.objects.filter(status='Reject').count()
    p=Notes.objects.filter(status='pending').count()
    all=Notes.objects.all().count()
    d={'a':a,'r':r,'p':p,'all':all}
    return render(request,'admin_home.html',d)


def Logout(request):
    return redirect('home')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Signup.objects.get(user=user)
    d={'data':data,'user':user}
    return render(request,'profile.html',d)


def changepwd(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=="POST":
        opwd=request.POST['old']
        newp=request.POST['new']
        cp=request.POST['confirm']
        if newp==cp:
            u=User.objects.get(username=request.user.username)
            u.set_password(newp)
            u.save()
            error="no"
        else:
            error="yes"
    d={"error":error}            
    return render(request,"changepwd.html",d)
#here start edit profile

def edit_pro(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user=User.objects.get(id=request.user.id)
    data=Signup.objects.get(user=user)
    error=False
    if request.method=='POST':
      f=request.POST['fname']
      l=request.POST['lname']
      contact=request.POST['contact']
      branch=request.POST['branch']  
      user.first_name=f
      user.last_name=l
      data.contact=contact
      data.branch=branch
      user.save()
      data.save()
      error=True
    d={'data':data,'user':user,'error':error}
    return render(request,'edit_profile.html',d)

#upload notes funtion start 
def uploadnotes(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method=="POST":
       b=request.POST['branch']
       s=request.POST['subject']
       n=request.FILES.get('notesfile')
       f=request.POST['filetype']
       d=request.POST['description']
       u=User.objects.filter(username=request.user.username).first()
       
       try:
           Notes.objects.create(user=u,uploadingdate=date.today()
                                ,branch=b,subject=s,notesfile=n,filetype=f,description=d,status='pending')
           error="no"
       except:
            error='yes'
    d={'error':error}         
    return render(request,'uploadtnotes.html',d)
# here views funtions is start
def viewnotes(request):
     if not request.user.is_authenticated:
        return redirect('login')
     user=User.objects.get(id=request.user.id)
     Note=Notes.objects.filter(user=user)
     d={'note':Note}
     return render(request,'view_note.html',d)

# here delete function is start 
def deletenotes(request,pid):
    if not request.user.is_authenticated:
        return redirect("login")
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('view_notes')

def deletenotes1(request,pid):
    if not request.user.is_authenticated:
        return redirect("login")
    notes=Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewall_note')

def viewuser(request):
    if not request.user.is_authenticated:
        return redirect('admin')
    users=Signup.objects.all()
    d={'users':users}
    return render(request,'view_user.html',d)

def delete_user(request,uid):
    if not request.user.is_authenticated:
        return redirect('admin')
    user=User.objects.get(id=uid)
    user.delete()
    return redirect('view_user')
def pending(request):
    if not request.user.is_authenticated:
        return redirect('admin')
    notes=Notes.objects.filter(status='pending')
    d={'notes':notes}
    return render(request,'pending.html',d)

#assign status start here
def assign(request,id):
    if not request.user.is_authenticated:
        return redirect('admin')
    notes =Notes.objects.get(id=id)
    error=""
    if request.method=="POST":
        s=request.POST['status']
        try:
            notes.status=s
            notes.save()
            error="no"
        except:
            error="yes"    
     
    d={'notes':notes,'error':error,'id':id}
    return render(request,'assign_status.html',d)
# Acceped status
def accept_notes(request):
    if not request.user.is_authenticated:
        return redirect("admin")
    notes=Notes.objects.filter(status='Accept')
    d={'notes':notes}
    return render(request,'accept_notes.html',d)

# rejected notes start here
def reject_notes(request):
    if not request.user.is_authenticated:
        return render("admin")
    notes=Notes.objects.filter(status="Reject")
    d={'notes':notes}
    return render(request,'reject_notes.html',d) 
# all notes function start here
def all_notes(request):
    if not request.user.is_authenticated:
        return render('admin')
    notes=Notes.objects.all()
    d={'notes':notes}
    return render(request,'all_notes.html',d)  
# delete the all notes
def delete_notes(request,id):
    if not request.user.is_authenticated:
        return redirect('admin')
    error=""
    notes=Notes.objects.get(id=id)
    try:
       notes.delete()
       error="no"
    except:
        error="yes"
    d={'error':error} 
    return render(request,"all_notes.html",d)
# view all notes with user side
def viewall_note(request):
    if not request.user.is_authenticated:
        return redirect("login")
    notes=Notes.objects.all()
    d={'notes':notes}
    return render(request,'viewuser_allnotes.html',d)     
