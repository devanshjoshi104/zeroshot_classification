from django.urls import path
from classifier import views

urlpatterns = [
    path('classify/', views.classify_text, name='classify_text'),
]
