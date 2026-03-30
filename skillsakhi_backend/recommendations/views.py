from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from users.models import UserProfile
from .models import Career, Recommendation
from .serializers import CareerSerializer, CourseSerializer, JobSerializer
from ml_model.recommender import rule_based_careers, recommend_by_model


def _get_profile(user):
    return UserProfile.objects.filter(user=user).prefetch_related('existing_skills').first()


@api_view(['GET'])
def career_recommendation_view(request):
    profile = _get_profile(request.user)
    if not profile:
        return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    model_output = recommend_by_model(profile)
    model_career_name, score = model_output if model_output else (None, 0.6)
    rule_career_names = rule_based_careers(profile)

    candidates = list(Career.objects.filter(name__in=rule_career_names))
    if model_career_name:
        model_career = Career.objects.filter(name=model_career_name).first()
        if model_career:
            candidates = [model_career] + [c for c in candidates if c.id != model_career.id]

    if not candidates:
        candidates = list(Career.objects.all()[:3])

    best = candidates[0]
    Recommendation.objects.create(user=request.user, career=best, suitability_score=score)

    return Response({
        'recommended_career': CareerSerializer(best).data,
        'alternative_careers': CareerSerializer(candidates[1:3], many=True).data,
        'suitability_score': round(score * 100, 2),
    })


@api_view(['GET'])
def skill_gap_view(request):
    profile = _get_profile(request.user)
    if not profile:
        return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

    latest = Recommendation.objects.filter(user=request.user).select_related('career').order_by('-created_at').first()
    if not latest:
        return Response({'detail': 'No recommendation found. Call /career-recommendation first.'}, status=400)

    required = [cs.skill.name for cs in latest.career.career_skills.select_related('skill')]
    user_skills = [s.name for s in profile.existing_skills.all()]
    missing = [s for s in required if s not in user_skills]
    match_pct = 0 if not required else round((len(required) - len(missing)) / len(required) * 100, 2)

    return Response({
        'recommended_career': latest.career.name,
        'required_skills': required,
        'user_skills': user_skills,
        'skill_gap': missing,
        'skill_match_percentage': match_pct,
    })


@api_view(['GET'])
def courses_view(request):
    latest = Recommendation.objects.filter(user=request.user).select_related('career').order_by('-created_at').first()
    if not latest:
        return Response({'detail': 'No recommendation found.'}, status=400)
    courses = latest.career.courses.all()
    return Response(CourseSerializer(courses, many=True).data)


@api_view(['GET'])
def jobs_view(request):
    latest = Recommendation.objects.filter(user=request.user).select_related('career').order_by('-created_at').first()
    if not latest:
        return Response({'detail': 'No recommendation found.'}, status=400)
    jobs = latest.career.jobs.all()
    return Response(JobSerializer(jobs, many=True).data)
