from django.urls import path
from .views import games, single_review

urlpatterns = [
    path('games/',games,name='games'),
    path('games/<int:game_id>',single_review,name='single_review'),
]
