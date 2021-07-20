
from django.urls   import path
from dog.views     import OwnerView, DogView

urlpatterns = [
    path('/dog', DogView.as_view()),
    path('/owner', OwnerView.as_view()),
]