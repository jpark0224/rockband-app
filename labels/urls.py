from django.urls import path
from .views import LabelListView, LabelDetailView

urlpatterns = [
    path('', LabelListView.as_view()),
    path('<str:pk>/', LabelDetailView.as_view())
]
