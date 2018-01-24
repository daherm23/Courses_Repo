# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors.append("Course Name needs to be more than 5 characters")
        if len(postData['desc']) < 15:
            errors.append("description must be greater than 15")
        return errors



class Course(models.Model):
	Name = models.CharField(max_length=255)
	Desc = models.CharField(max_length=255, default=1)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects= BlogManager() 




# Create your models here.
