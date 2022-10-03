from django.urls import path

from car.views import CarView, UserView

urlpatterns = [
    path('', CarView.as_view()),
    path('user', UserView.as_view())
]
