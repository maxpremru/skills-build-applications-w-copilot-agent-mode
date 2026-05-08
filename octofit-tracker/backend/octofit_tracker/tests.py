from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(str(team), "Test Team")

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=team)
        self.assertEqual(str(user), "testuser")
        self.assertEqual(user.team, team)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=team)
        activity = Activity.objects.create(user=user, type="run", duration=30, distance=5.0)
        self.assertEqual(str(activity), "test@example.com - run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Cardio", description="Cardio session")
        self.assertEqual(str(workout), "Cardio")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(str(leaderboard), "test@example.com - 100")
