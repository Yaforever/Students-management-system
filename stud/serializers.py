from rest_framework import serializers
from .models import Group, Student
from django.db.models.fields import DateField


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ('id', 'groupname', 'mainstudent')


class StudentSerializer(serializers.ModelSerializer):
	date = serializers.DateField(format="%Y-%B-%d")

	class Meta:
		model = Student
		fields = ('id','name', 'num', 'group', 'date')
