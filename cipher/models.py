# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CaesarCipher( models.Model):
    user = models.CharField(max_length=68, null=True)
    decrypt_text = models.TextField(null=False)
    encrypt_text = models.TextField(null=False)
    keys = models.IntegerField(default=0, null=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'caesar_cipher'

    def __str__(self):
        return "%s | %s " % (self.user, self.date)

