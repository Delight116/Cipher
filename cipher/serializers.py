from rest_framework import serializers
from cipher.models import CaesarCipher


class CodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CaesarCipher
        fields = '__all__'
