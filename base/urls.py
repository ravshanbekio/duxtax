from django.urls import path
from .views import DashboardView, CarModelView, Car2ModelView

urlpatterns = [
    path('',DashboardView.as_view(),name='dashboard'),
    path('car/<int:car_id>/',CarModelView.as_view(), name='car_details'),
    path('car/<int:car_id>/add', Car2ModelView.as_view(), name='car_make_model'),
]