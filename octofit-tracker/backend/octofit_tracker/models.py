from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.SET_NULL, null=True)
    is_superhero = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, related_name='activities', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    date = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.type} ({self.date})"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField(User, related_name='suggested_workouts', blank=True)

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    user = models.ForeignKey(User, related_name='leaderboard_entries', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.name} - {self.score}"
