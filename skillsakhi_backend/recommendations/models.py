from django.db import models
from django.contrib.auth.models import User
from users.models import Skill


class Career(models.Model):
    name = models.CharField(max_length=120, unique=True)
    min_education = models.CharField(max_length=100)
    demand_level = models.CharField(max_length=20)
    work_preference = models.CharField(max_length=20)
    interest_tags = models.TextField(help_text='Comma separated tags')

    def __str__(self):
        return self.name


class CareerSkill(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='career_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('career', 'skill')


class Course(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    provider = models.CharField(max_length=100)
    link = models.URLField()
    estimated_duration = models.CharField(max_length=50)


class Job(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    source = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    link = models.URLField()


class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    suitability_score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
