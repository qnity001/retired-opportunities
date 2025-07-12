from django.urls import path
from .views import get_pdf_summaries

urlpatterns = [
    path('api/summaries/', get_pdf_summaries),
]
