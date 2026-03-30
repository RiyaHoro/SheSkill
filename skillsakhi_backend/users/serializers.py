from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Skill


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class UserProfileSerializer(serializers.ModelSerializer):
    existing_skills = serializers.ListField(child=serializers.CharField(), write_only=True)
    skill_objects = SkillSerializer(source='existing_skills', many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'age',
            'education_level',
            'location',
            'interests',
            'work_preference',
            'existing_skills',
            'skill_objects',
        ]

    def create(self, validated_data):
        skills = validated_data.pop('existing_skills', [])
        profile, _ = UserProfile.objects.update_or_create(
            user=self.context['request'].user,
            defaults=validated_data,
        )
        profile.existing_skills.clear()
        for skill_name in skills:
            skill, _ = Skill.objects.get_or_create(name=skill_name.strip().lower())
            profile.existing_skills.add(skill)
        return profile
