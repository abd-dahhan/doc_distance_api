from django.urls import path
from .api_views import TextToList, WordFreq, SimilarityScore

urlpatterns = [
    path("text-to-list/", TextToList.as_view(), name="text-to-list"),
    path("get-frequencies/", WordFreq.as_view(), name="word-frequencies"),
    path("similarity-score/", SimilarityScore.as_view(), name="similarity-score"),
]
