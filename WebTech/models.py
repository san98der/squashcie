from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib import admin

class Pool(models.Model):
	name = models.CharField(max_length=30)

class Player(User):
	name = models.CharField(max_length=200)
	matches_won = models.IntegerField()
	sets_won = models.IntegerField()
	points_scored = models.IntegerField()
	points_against = models.IntegerField()
	pool = models.ForeignKey(Pool, null=True, on_delete=models.SET_NULL)

class Match(models.Model):
	mID = models.IntegerField()
	player1 = models.ForeignKey(Player, null=True, related_name='p1', on_delete=models.CASCADE)
	player2 = models.ForeignKey(Player, null=True, related_name='p2', on_delete=models.CASCADE)
	p1_s1_score = models.IntegerField()
	p2_s1_score = models.IntegerField()
	p1_s2_score = models.IntegerField()
	p2_s2_score = models.IntegerField()
	p1_s3_score = models.IntegerField()
	p2_s3_score = models.IntegerField()
	date = models.CharField(max_length=30)
	pool = models.ForeignKey(Pool, null=True, on_delete=models.SET_NULL)
