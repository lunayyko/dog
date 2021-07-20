from django.urls import path, include

urlpatterns = [
    path('dog', include('dog.urls'))
]
