import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
	def post(self, request):
		data = json.loads(request.body)
		Owner.objects.create(
			name = data['name'],
			email = data['email'],
			age = data['age'],
		)		

		return JsonResponse({'message':'created'}, status=201)


	def get(self, request):
		owners = Owner.objects.all()
		results = []

		for owner in owners:
			
			dog_list = []
			dogs = owner.dog_set.all()   # 역참조는 이름_set, 해당 관련강아지는 다 가져와야하니까 all()
			for dog in dogs:
				dog_list.append(
        			{
						'dog_name' : dog.name,
						'dog_age': dog.age,
					}			
				)

			results.append(
				{
					'name' : owner.name,
					'email' : owner.email,
					'age' : owner.age,
					'dogs' : dog_list,
				}
			)
   
		return JsonResponse({'results':results}, status=200)

class DogsView(View):
	def post(self, request):
		data = json.loads(request.body)
		# print(data)
		owner = Owner.objects.get(name=data['owner_name'])
		Dog.objects.create(
			name = data['name'],
			age = data['age'],
			owner = owner,
		)

		return JsonResponse({'message':'created'}, status=201)



