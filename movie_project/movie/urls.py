from django.urls   import path
# from dog.views     import OwnerView, DogView
#OwnerView, DogView 는 view.py로부터 get, post 기능을 수행하는 클래스를 import해온다.

urlpatterns = [
    # path('/dog', DogView.as_view()),
    # path('/owner', OwnerView.as_view()),
    #as_view는 해당 경로까지 온 요청이 어떤 method인지 판단해주는 함수이다.
]