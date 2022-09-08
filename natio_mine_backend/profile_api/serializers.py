from dataclasses import fields
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('experience','operation_in_progress')

    def update(self, instance, validated_data):

        instance.experience = validated_data["experience"]
        instance.operation_in_progress = validated_data["operation_in_progress"]

        instance.save()

        return instance