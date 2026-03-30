from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    WORK_PREFERENCE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('wfh', 'Work From Home'),
        ('freelancing', 'Freelancing'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveIntegerField()
    education_level = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    interests = models.TextField(help_text='Comma separated interests')
    work_preference = models.CharField(max_length=20, choices=WORK_PREFERENCE_CHOICES)
    existing_skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
