from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        workout = Workout.objects.create(name='Super Strength', description='Strength training', difficulty='Hard')
        activity = Activity.objects.create(user=user, type='Run', duration=30, date='2026-04-13')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

    def test_team(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
