from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_task_category, name='add_task_category'),
]
