from django.urls import path
from .views import career_recommendation_view, skill_gap_view, courses_view, jobs_view

urlpatterns = [
    path('career-recommendation', career_recommendation_view),
    path('skill-gap', skill_gap_view),
    path('courses', courses_view),
    path('jobs', jobs_view),
]
