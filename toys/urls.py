from django.urls import path
from .views import ToyList, ToyDetail


urlpatterns = [
    path("", ToyList.as_view(), name="toy_list"),
    path("<int:pk>/", ToyDetail.as_view(), name="toy_detail"),
]
