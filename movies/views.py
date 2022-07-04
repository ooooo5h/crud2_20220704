import json

from django.http import JsonResponse
from django.views import View

from movies.models import Actor, Movie, ActorAndMoive

class ActorsView(View):
	def post(self, request):
		data = json.loads(request.body)
		Actor.objects.create(
			first_name = data['first_name'],
			last_name = data['last_name'],
			date_of_birth = data['date_of_birth'],
		)
		return JsonResponse({'Message':'Actor created'}, status=201)

	def get(self, request):
		
		actors = Actor.objects.all()
		results = []

		for actor in actors:
			movies = []

			results.append(
				{
					'first_name' : actor.first_name,
					'last_name' : actor.last_name,
					'movies' : movies,
			})
		return JsonResponse({'results':results}, status=200)
	
