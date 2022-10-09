from rest_framework import serializers
from .models import User, Student, StudentProgress
from courses.models import Course, Skill

# converting python objects to JSON file formats
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    # hashing the password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course    

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill    

class StudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True, many=True)
    skill = SkillSerializer(read_only=True, many=True)
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'gender', 'course', 'joined_courses', 'skill', 'skills')
        