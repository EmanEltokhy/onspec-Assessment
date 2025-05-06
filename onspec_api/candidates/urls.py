from django.urls import path
from .views import CandidateView

urlpatterns = [
    path('candidates/', CandidateView.as_view(), name='candidate')
]
