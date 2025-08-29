from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Example models for demonstration (should be replaced with actual app models)
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        app_models.Team.objects.all().delete()
        app_models.UserProfile.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Team Marvel')
        dc = app_models.Team.objects.create(name='Team DC')

        # Create users (super heroes)
        users = [
            app_models.UserProfile.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            app_models.UserProfile.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            app_models.UserProfile.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            app_models.UserProfile.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create activities
        for user in users:
            app_models.Activity.objects.create(user=user, type='Running', duration=30)
            app_models.Activity.objects.create(user=user, type='Cycling', duration=45)

        # Create workouts
        for user in users:
            app_models.Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session')

        # Create leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=100)
        app_models.Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
