from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet, api_root
import os

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

CODESPACE_NAME = os.environ.get('CODESPACE_NAME', 'localhost')
BASE_API_URL = f"https://{CODESPACE_NAME}-8000.app.github.dev/api/"

urlpatterns = [
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
