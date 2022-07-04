from django.urls import path
from movies.views import ActorsView

urlpatterns = [
	path('/actors', ActorsView.as_view()),
]
