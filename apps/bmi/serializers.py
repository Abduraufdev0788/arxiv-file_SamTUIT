from rest_framework import serializers
from .models import Talaba, BitiruMalakaviyIsh, Fayl, Baholash

class TalabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talaba
        fields = "__all__"


class BitiruMalakaviyIshSerializer(serializers.ModelSerializer):
    class Meta:
        model = BitiruMalakaviyIsh
        fields = [
            'id', 
            'talaba', 
            'mavzu', 
            'ilmiy_rahbar',
            'taqdimot_sanasi',
            'holat', 
            'ball',
            'izoh', 
            'yuklangan_sana',
            'yangilangan_sana'
         ]


class FaylSerializer(serializers.ModelSerializer):
    bitiruv_ishi = BitiruMalakaviyIshSerializer(read_only=True)

    class Meta:
        model = Fayl
        fields = [
            'id', 
            'bitiruv_ishi',
            'fayl', 
            'fayl_turi', 
            'nomi', 
            'yuklangan_sana'
        ]

class BaholashSerializer(serializers.ModelSerializer):
    bitiruv_ishi = BitiruMalakaviyIshSerializer(read_only=True)

    class Meta:
        model = Baholash
        fields = [
            'id', 
            'bitiruv_ishi', 
            'baholovchi', 
            'ball', 
            'izoh', 
            'sana'
        ]
