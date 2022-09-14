from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='dashboard-index'),
        path('inpatient/', views.inpatient, name='dashboard-inpatient'),

]

