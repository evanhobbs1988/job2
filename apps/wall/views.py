from django.shortcuts import render, redirect
from .models import job
from django.contrib import messages
from ..login.models import User
from django.db.models import Count

def index(request):
    if not "current_user" in request.session:
        messages.add_message(request, messages.INFO, "Must be logged in to view this page")
        return redirect('login:index')

    context = {
        "users": User.objects.all,
        "jobs": job.objects.order_by('-created_at'),
        "current_user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'wall/index.html', context)

def add_job(request):
    if request.method == "POST":
        new_post = job.objects.process_secret(request.POST, request.session['user_id'])
        print (new_post.post)
        return redirect('wall:index')


def delete_job(request):
    post_to_delete = job.objects.get(id=request.POST['job_id'])
    post_to_delete.delete()
    return redirect('wall:index')

def delete_job2(request):
    post_to_delete = job.objects.get(id=request.POST['job_id'])
    post_to_delete.delete()
    return redirect('wall:most_popular')

def logout(request):
    request.session.clear()
    return redirect('login:index')
