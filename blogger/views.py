import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import RegistrationForm, EditProfileForm
from django.conf import settings
from django.template.context_processors import media
from django.core.files.storage import default_storage

def index(request):
    title = "BlogFIRE"
    return render(request, 'index.html' , {'title': title})

@login_required
def home(request):
    title = "BlogFIRE"
    #media_path =  settings.MEDIA_ROOT
    #img_obj = BloggerPic.objects.get(bloguser=BloggerProfile.objects.get(user=request.user))
    #if img_obj is not None:
       # pic_path = img_obj.profile_pic
    return render(request, 'redirect.html' , {'title': title})

@login_required
def bloggerprofile(request):
    title = "Blogger"
    return render(request, 'profile.html' , {'title': title})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.bloggerprofile.mobile_no = form.cleaned_data.get('mobile_no')
            user.bloggerprofile.email_id = form.cleaned_data.get('email_id')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def edit_bloggerprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user )
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.bloggerprofile.email_id = form.data.get('email_id')
            user.bloggerprofile.birth_date = form.data.get('birth_date')
            user.bloggerprofile.home_town = form.data.get('home_town')
            user.bloggerprofile.bio = form.data.get('bio')
            user.bloggerprofile.hobbies = form.data.get('hobbies')
            user.save()
        
        
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'editprofile.html', {'form': form})

@login_required
def profile_picUploadSave(request):
    try:
        if request.method=='POST':
            if request.FILES:
                file_temp=request.FILES['file']
                f_name=str(file_temp)
                media_path =  settings.MEDIA_ROOT
                file_dir = os.path.join(media_path, "profile_pic", str(request.user))
                # save image using default storage
                if os.path.isdir(file_dir) == False :
                    os.mkdir(file_dir)
                
                file_path = os.path.join(file_dir,f_name)
                file_save = default_storage.save(file_path,file_temp) 
                # save to the model
                bloger_pic_obj = BloggerPic(
                                bloguser=BloggerProfile.objects.get(user=request.user),
                                profile_pic="profile_pic/"+str(request.user)+"/"+f_name,
                    )
                bloger_pic_obj.save()
                img_path = "profile_pic/"+str(request.user)+"/"+f_name
                return Response({"image_url":img_path})
        return render(request,"editprofile.html",{})
    except Exception as e:
        print(str(e))
        return render(request,"error.html",{"msg":"back to previous page"})


# obj = BloggerPic.object.get(bloguser=BloggerProfile.objects.get(user=request.user))
# if obj is not None:
#     pic_path = obj.profile_pic