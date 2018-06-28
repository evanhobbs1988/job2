from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from django.db.models import Count


class JobManager(models.Manager):
    def process_job(self, postData, user_id):
        job = job.objects.create(post = postData['job'], creator = User.objects.get(id=user_id))
        return job



class job(models.Model):
    post = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    creator = models.ForeignKey(User, related_name="creator", null=True, on_delete="CASCADE")
    

    objects = JobManager()
