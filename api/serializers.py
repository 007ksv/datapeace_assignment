from rest_framework import serializers
from .models import CustomUser


# Defining CustomUserSerializer for serializing and deserializing purpose


class CustomUserSerializer(serializers.ModelSerializer):

	class Meta:

		model = CustomUser
		fields = '__all__'			# Getting all fields of model in action

