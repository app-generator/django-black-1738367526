# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Equipment(models.Model):

    #__Equipment_FIELDS__
    inventory = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Equipment_FIELDS__END

    class Meta:
        verbose_name        = _("Equipment")
        verbose_name_plural = _("Equipment")


class Sysusers(models.Model):

    #__Sysusers_FIELDS__
    name = models.BooleanField()

    #__Sysusers_FIELDS__END

    class Meta:
        verbose_name        = _("Sysusers")
        verbose_name_plural = _("Sysusers")



#__MODELS__END
