from rest_framework import serializers
from users.serializers import SkillSerializer
from .models import Career, Course, Job


class CareerSerializer(serializers.ModelSerializer):
    required_skills = serializers.SerializerMethodField()

    class Meta:
        model = Career
        fields = ['id', 'name', 'min_education', 'demand_level', 'work_preference', 'required_skills']

    def get_required_skills(self, obj):
        return [cs.skill.name for cs in obj.career_skills.select_related('skill').all()]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['title', 'provider', 'link', 'estimated_duration']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'company', 'source', 'location', 'link']
