from django.core.management.base import BaseCommand
from recommendations.management_seed import seed


class Command(BaseCommand):
    help = 'Seed careers, skills, courses and jobs.'

    def handle(self, *args, **options):
        seed()
        self.stdout.write(self.style.SUCCESS('Seed data inserted/updated.'))
