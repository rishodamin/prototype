from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Works, Details, PostJobs

# Create your views here.
def index(req):
    if not req.user.is_authenticated:
        return redirect('/login')
    detail = Details.objects.filter(username=req.user.username).first()
    content = {"detail":detail}
    return render(req, 'index.html', content)

def hire(req, ind):
    content = {"ind":str(int(ind)+6)}
    content["works"] = Works.objects.filter(IntId__range=(int(ind), int(ind)+5)).values()
    return render(req, 'hire.html', content)

def book(req, ind):
    content = {"ind":str(int(ind)+6)}
    content["works"] = Works.objects.filter(IntId__range=(int(ind), int(ind)+5)).values()
    return render(req, 'book.html', content)

def login(req):
    if req.method=="POST":
        username = req.POST["username"]
        password = req.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect("/")
        messages.info(req, "Credentials Invalid")
        return redirect("login")
    return render(req, "login.html")

def logout(req):
    auth.logout(req)
    return redirect('login')

def register(req):
    if req.method=="POST":
        username = req.POST["username"]
        email = req.POST["email"]
        password = req.POST["password"]
        password2 = req.POST["password2"]
        num = req.POST["phonenumber"]
        name = req.POST["fullname"]
        if not username:
            messages.info(req, "Username not given")
            return redirect("register")
        if not name:
            messages.info(req, "Name not given")
            return redirect("register")
        if Details.objects.filter(phonenum=num).exists():
            messages.info(req, "Phone Number already used")
            return redirect("register")
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(req, "Email already used")
                return redirect("register")
            if User.objects.filter(username=username).exists():
                messages.info(req, "username already used")
                return redirect("register")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            detail = Details(username=username, name=name, phonenum=num)
            detail.save()
            return redirect("login")
        messages.info(req, "Password not the same")
        return redirect("register")
    
    return render(req, "register.html")

def postjobs(req, categ):
    if req.method=="POST":
        name = req.POST['name']
        date = req.POST['date']
        time = req.POST['time']
        strength = req.POST['strength']
        menWage = req.POST['menWage']
        womenWage = req.POST['womenWage']
        phonenum = req.POST['phonenum']
        town = req.POST['town']
        address = req.POST['address']
        description = req.POST['description']
        if ((not date) or (not time) or (not strength) or (not menWage)
             or (not womenWage) or (not phonenum) or (not town) or (not address)):
            messages.info(req, "Some fields need to be fill")
            return redirect("/postjobs/"+categ)
        post = PostJobs(name=name, username=req.user.username, category=categ,
                        date=date, time=time, strength=strength, 
                        menWage=menWage, womenWage=womenWage, phonenum=phonenum, 
                        town=town, address=address, description=description)
        post.save()
        post.strId = str(post.id)
        post.save()
        return redirect("/")
    
    return render(req, "postjobs.html", {"categ":categ})

def getjobs(req, categ):
    content = {"categ":categ}
    content['posts'] = PostJobs.objects.filter(category=categ).all()
    return render(req, "getjobs.html", content)

def jobdetails(req, jobid):
    content = {}
    content['post'] = PostJobs.objects.filter(id=jobid).first()
    return render(req, "jobdetails.html", content)