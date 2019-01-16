from django.urls import path
from .apiviews import PersonList, PersonDetail
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path("person/", PersonList.as_view(), name="person_list"),
    path("person/<int:pk>/", PersonDetail.as_view(), name="person_detail"),
    path(r"swagger-docs/", schema_view),
]
