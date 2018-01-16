import operator

def rank(Pool):
	players = Player.objects.get(pool = Pool)
	players = sorted(players, key=operator.attrgetter('points_scored')
	players = sorted(players, key=operator.attrgetter('sets_won')
	players = sorted(players, key=operator.attrgetter('matches_won')
	players = reversed(players)
	return players