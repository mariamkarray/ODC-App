from rest_framework import serializers
from courses.models import Course, Skill, Supplier

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = ['name', 'description', 'prerequisite_courses']
    
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']  