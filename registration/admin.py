'''
Created on 25 May 2012

@author: euan
'''
from django.contrib import admin

from registration import models

admin.site.register(models.OffSiteInvite)
admin.site.register(models.URLToken)