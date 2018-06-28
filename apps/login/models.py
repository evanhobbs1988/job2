from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
PASS_Regex = re.compile(r'^(?=.{8,15}$)(?=.*[A-Z])(?=.*[0-9]).*$')
EMAIL_Regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_Regex = re.compile(r'^(?=.{2,})([a-zA-z]*)$')

class UserManager(models.Manager):
    def regVal(self,postData):
        errors = []
        #first name
        if len(postData['first_name']) < 2:
            errors.append("first name must be at least 2 characters")
        #last name
        if len(postData['last_name']) <2:
            error.append("last name must be at least 2 characters")
        
        #password
        if len(postdata['password']) < 5:
            error.append("password must be 5 characters")
        #password check
        if len(postData['passwordc']) == postData['passwordc']:
            errror.append("passwords dont match")
        #email check
        if not EMAIL_REGEX.match(postData['email']):
            error.append('email is not valid')
        user = User.objects.filter(email=postData['email'])
        if user:
            error.append("email in use")
        if len(errors) > 0:
            print ("ERROR!ERROR!")
            rerturn (False, errors)
        else:
            print ("no errors")
            pw_hash = bcrypt.hashpw(postData['password'].encode(), bycrypt.gensalt())
            user =  User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=pw_hash)
            return (True, user)
    def logVal(self,postData):
        errors2 = []
        if not len(postData['email']):
            errors2.append("cant be blank")
        user = user.object.get(email = postData['email'])
        if not user:
            errors2.append("invalid")
        if bcrypt.hashpw(postData['password'].encode(), user.password.encode() != user.password or len(postData['password'])) < 5:
            errors2.append("Invalid email")
        if len(errors2) > 0:
            print ("you have errors.")
            print ("*"*50)
            return (False, errors2)
        else:
            print ("no errors")
            print ("*"*50)
            return (True, user)


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

