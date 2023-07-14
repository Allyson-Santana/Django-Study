from django.urls import path
from . import views

urlpatterns = [
    path('acid_atomic', views.acid_atomic, name="acid_atomic"),
    path('register_people', views.register_people, name="register_people"),
    path('aggregate', views.aggregate, name="aggregate"),
    path('annotate', views.annotate, name="annotate"),
]