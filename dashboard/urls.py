from django.urls import path
from . import views
from .views import AddPatientView
urlpatterns = [
        path('dashboard/', views.index, name='dashboard-index'),
        path('form/', AddPatientView.as_view(), name='dashboard-inpatient-form'),
       
        path('inpatient/delete/<int:pk>/', views.inpatient_delete, name='dashboard-inpatient-delete'),
       # path('inpatient/edit/<int:pk>/', views.inpatient_edit, name='dashboard-inpatient-edit'),

        path('inpatient/', views.inpatient, name='dashboard-inpatient'),


]

