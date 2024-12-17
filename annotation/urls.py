from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('annotate/<int:task_id>/', views.annotate_task, name='annotate_task'),
]
