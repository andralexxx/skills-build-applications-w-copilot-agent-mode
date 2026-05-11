from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Team, User, Workout, Activity, Leaderboard

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=self.team)
        self.workout = Workout.objects.create(name='Run', description='Running workout')
        self.activity = Activity.objects.create(user=self.user, workout=self.workout, duration=30)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)

    def test_users_endpoint(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, 200)

    def test_workouts_endpoint(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, 200)

    def test_activities_endpoint(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_endpoint(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, 200)

    def test_api_root_links(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
