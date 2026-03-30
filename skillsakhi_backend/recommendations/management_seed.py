from users.models import Skill
from recommendations.models import Career, CareerSkill, Course, Job

CAREER_DATA = {
    'Data Analyst': {
        'education': 'graduate',
        'demand': 'high',
        'work_preference': 'full_time',
        'tags': 'analysis,data',
        'skills': ['sql', 'excel', 'python', 'power bi'],
    },
    'Food Blogger': {
        'education': 'basic',
        'demand': 'high',
        'work_preference': 'wfh',
        'tags': 'cooking,content',
        'skills': ['content writing', 'photography', 'seo'],
    },
    'Graphic Designer': {
        'education': 'intermediate',
        'demand': 'high',
        'work_preference': 'freelancing',
        'tags': 'design,creativity',
        'skills': ['canva', 'adobe photoshop', 'branding'],
    },
}


def seed():
    for name, details in CAREER_DATA.items():
        career, _ = Career.objects.get_or_create(
            name=name,
            defaults={
                'min_education': details['education'],
                'demand_level': details['demand'],
                'work_preference': details['work_preference'],
                'interest_tags': details['tags'],
            },
        )
        for skill_name in details['skills']:
            skill, _ = Skill.objects.get_or_create(name=skill_name)
            CareerSkill.objects.get_or_create(career=career, skill=skill)

        Course.objects.get_or_create(
            career=career,
            title=f'Career Starter: {name}',
            provider='Coursera',
            link='https://www.coursera.org',
            estimated_duration='6 weeks',
        )
        Job.objects.get_or_create(
            career=career,
            title=f'Junior {name}',
            company='Example Corp',
            source='LinkedIn',
            location='Remote',
            link='https://www.linkedin.com/jobs/',
        )
