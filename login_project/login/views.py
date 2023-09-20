from django.shortcuts import  render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import Studentform

@login_required(login_url='login')
def home_page(request):
    student_list = Student.objects.all()
    return render(request, 'registration/home.html',{'student_list': student_list})

def signuppage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        email= request.POST.get('email')
        pw1= request.POST.get('password1')
        pw2= request.POST.get('password2')
        
        if pw1!=pw2:
            return HttpResponse('your password and confirm password are not same!!')
        else:
            my_user = User.objects.create_user(username,email,pw1)
            my_user.save
            return redirect ('login')
        
    return render(request, "registration/signup.html")

def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        #user = authenticate(request, username=)
        print(user)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            return HttpResponse('Username or Password is incorrect!')
    return render(request, 'registration/login.html')

def add_student(request):
    form = Studentform(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'registration/add_student.html', {'form':form})

def update_student_info(request, student_id):
    student_data = Student.objects.get(pk = student_id)
    form = Studentform(request.POST or None, instance=student_data)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'registration/update_student_info.html',{'student_data': student_data, 'form':form })
    
def delete_student(request, student_id):
    delete_data = Student.objects.get(pk = student_id)
    delete_data.delete()
    return redirect('home')
    
    
def logout(request):
    logout(request)
    return redirect ('login')
