# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import views, generics, viewsets, mixins

from django.shortcuts import render
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from cipher.models import CaesarCipher
from cipher.serializers import CodeSerializers
from cipher.helpers import encrypt_texts, decrypt_texts, searchKey, get_key_cipher


# Create your views here.
class EncryptText(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = CaesarCipher.objects.all()
    serializer_class = CodeSerializers
    permission_classes = (AllowAny,)

    @list_route(methods=['POST'])
    def encrypt(self, request):
        text = encrypt_texts(request.data.get('text'), request.data.get('key'))
        cc = CaesarCipher.objects.create(
            decrypt_text=request.data.get('text'),
            encrypt_text=text,
            keys=request.data.get('key')
        )
        cc.save()
        return Response({'encrypt': True})

    @list_route(methods=['POST'])
    def decrypt(self, request):
        key = searchKey(request.data.get('text'))
        print(key)
        result = decrypt_texts(request.data.get('text'), int(key))
        if not result:
            return Response({'decrypt': False})

        print(result)

        # cc = CaesarCipher.objects.create(
        #     decrypt_text=result['text'],
        #     encrypt_text=request.data.get('text'),
        #     keys=result['key']
        # )
        # cc.save()
        return Response({'decrypt': True})
