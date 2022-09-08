from dataclasses import fields
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('experience',)

    def update(self, instance, validated_data):

        instance.experience = validated_data["experience"]
        instance.save()
        
        return instance