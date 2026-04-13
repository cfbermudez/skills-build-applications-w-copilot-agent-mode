from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data (delete individually to avoid ObjectId unhashable error)
        for model in [Leaderboard, Activity, User, Team, Workout]:
            for obj in model.objects.all():
                if getattr(obj, 'id', None) is not None:
                    obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard'),
            Workout.objects.create(name='Speed Run', description='High intensity running', difficulty='Medium'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Run', duration=30, date=timezone.now())
        Activity.objects.create(user=users[1], type='Swim', duration=45, date=timezone.now())
        Activity.objects.create(user=users[2], type='Bike', duration=60, date=timezone.now())
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date=timezone.now())

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
