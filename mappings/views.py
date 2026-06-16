from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import PatientDoctorMapping
from .serializers import MappingSerializer, MappingDetailSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MappingSerializer
        return MappingDetailSerializer

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        ).select_related('patient', 'doctor')

class MappingsByPatientView(generics.ListAPIView):
    serializer_class = MappingDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(
            patient_id=patient_id,
            patient__created_by=self.request.user,
        ).select_related('patient', 'doctor')

class MappingDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(
            patient__created_by=self.request.user
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Mapping removed successfully."},
            status=status.HTTP_200_OK,
        )