from django.urls import path

from .views import MappingListCreateView, MappingsByPatientView, MappingDeleteView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<uuid:patient_id>/', MappingsByPatientView.as_view(), name='mapping-by-patient'),
    path('delete/<uuid:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]