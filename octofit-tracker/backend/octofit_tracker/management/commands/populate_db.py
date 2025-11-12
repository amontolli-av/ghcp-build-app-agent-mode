from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            self.stdout.write(self.style.WARNING('Deleting old data...'))
            Leaderboard.objects.all().delete()
            Activity.objects.all().delete()
            Workout.objects.all().delete()
            User.objects.all().delete()
            Team.objects.all().delete()

            self.stdout.write(self.style.SUCCESS('Creating teams...'))
            marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
            dc = Team.objects.create(name='DC', description='DC superheroes')

            self.stdout.write(self.style.SUCCESS('Creating users...'))
            users = [
                User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
                User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
                User.objects.create(name='Hulk', email='hulk@marvel.com', team=marvel, is_superhero=True),
                User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
                User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True),
                User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            ]

            self.stdout.write(self.style.SUCCESS('Creating activities...'))
            Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-11-12')
            Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-11-11')
            Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-11-10')
            Activity.objects.create(user=users[3], type='Running', duration=25, date='2025-11-09')
            Activity.objects.create(user=users[4], type='Cycling', duration=50, date='2025-11-08')
            Activity.objects.create(user=users[5], type='Swimming', duration=70, date='2025-11-07')

            self.stdout.write(self.style.SUCCESS('Creating workouts...'))
            w1 = Workout.objects.create(name='Pushups', description='Upper body workout')
            w2 = Workout.objects.create(name='Situps', description='Core workout')
            w1.suggested_for.set([users[0], users[3]])
            w2.suggested_for.set([users[1], users[4]])

            self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
            Leaderboard.objects.create(user=users[0], score=100)
            Leaderboard.objects.create(user=users[1], score=90)
            Leaderboard.objects.create(user=users[2], score=80)
            Leaderboard.objects.create(user=users[3], score=95)
            Leaderboard.objects.create(user=users[4], score=85)
            Leaderboard.objects.create(user=users[5], score=75)

            self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
