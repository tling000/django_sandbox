from .views import (
    MemoListView, MemoDetailView)
from django.urls import path

urlpatterns = [
    path('', view=MemoListView.as_view()),
    path('<int:id>/', view=MemoDetailView.as_view())
]
