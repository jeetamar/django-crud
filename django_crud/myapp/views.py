
# Create your views here.
from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import UserForm
from .models import User
# Create your views here.

def home(request):
    if request.method == 'POST':
        form=UserForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # password=form.cleaned_data['password']
            # user_obj=User(name=name,email=email,password=password)
            # user_obj.save()
            form.save()
            print("form save")
            # message="User Registered"
            return redirect('/')
    else:
        form=UserForm()
        data=User.objects.all()
    return render(request,'home.html',{'form':form,'data':data})

def dete_user(request,id):
    # if request.method == 'POST':
    id=id
    user=User.objects.get(pk=id)
    user.delete()
    return redirect('/')

def update_user(request,id):
    id=id
    if request.method == 'POST':
        user_id = User.objects.get(pk=id)
        form_data=UserForm(request.POST,instance=user_id)
        if form_data.is_valid():
            form_data.save()
            print("USER Updated")
            return redirect('/')
    else:
        user_id = User.objects.get(pk=id)
        form_data = UserForm(instance=user_id)
    return render(request,'update.html',{'form':form_data})