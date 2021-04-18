from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:question_id>/', views.details, name="details"),
    path('<int:question_id>/results', views.results, name="results"),
    path('<int:question_id>/votes', views.vote, name="votes"),
    path('view_all_results', views.view_all_results, name="all_results"),
]
