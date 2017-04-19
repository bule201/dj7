# -*- coding: utf-8 -*-

from django.db import models

class Record(models.Model):
    num01 = models.IntegerField()
    num02 = models.IntegerField()
    ret = models.IntegerField()

