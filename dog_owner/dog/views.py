import json

from django.http import JsonResponse
from django.views import View

from .models import Dog, Owner

class OwnerView(View):
    def post(self, request):
        data  = json.loads(request.body)
        name = data['name']
        email= data['email']
        Owner.objects.create(name = name, email=email)        
        return JsonResponse({'Message':'Created'}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results=[]
        for owner in owners:
            results.append(
            {
                "name" : owner.name,
                "email" : owner.email,
                "dog_list" : [{"이름":dog.name} for dog in Dog.objects.filter(owner_id=owner.id)]
            }
        )
        return JsonResponse({'result':results}, status=200)

class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        name = data['name']
        owner = Owner.objects.get(name = data['owner'])
        # 프론트에서 준 데이터에서 오너의 이름을 가져오고 그걸 owner라는 변수에 대입 /Objects 출력
        dog = Dog.objects.create(name = name, owner = owner)
        return JsonResponse({'Message':'Created'}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results=[]
        for dog in dogs:
            results.append(
            {
                "name" : dog.name,
                "owner" : dog.owner.name
            }
        )
        return JsonResponse({'result':results}, status=200)