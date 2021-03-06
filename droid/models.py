from django.db import models
from analyze import get_permissions, get_name
# Create your models here.
import os
#class Document(models.Model):
 #   docfile = models.FileField(upload_to='documents/')
    #name = models.CharField(max_length=256, null=True)
    


class Permission(models.Model):
    name = models.CharField(max_length=512)    
    class Meta:
        ordering = ['name']    

    def __unicode__(self):
        return self.name

class APK(models.Model):
	apk = models.FileField(upload_to="apks/")
	name = models.CharField(max_length=256, null=True)
	permissions = models.ManyToManyField(Permission)
        permissions_loaded = models.BooleanField(default=False)
	
	def load_permissions(self,path):
	        self.permissions.clear()
        	for p in get_permissions(path):
 	           perm, created = Permission.objects.get_or_create(name=p)
 	           if created: perm.save()
 	           self.permissions.add(perm)
 	        self.permissions_loaded = True
        	self.save()
	def __unicode__(self):
        	return self.name
