from django.urls   import path
from movie.views     import MovieView, ActorView

urlpatterns = [
    path('/actor', ActorView.as_view()),
    path('/movie', MovieView.as_view()),
    #as_view는 해당 경로까지 온 요청이 어떤 method인지 판단해주는 함수이다.
]