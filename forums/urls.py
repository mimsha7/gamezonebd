from django.urls import path
from forums.views import forum


urlpatterns = [
    path('forum',forum,name='forum'),
]