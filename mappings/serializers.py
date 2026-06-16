from rest_framework import serializers

from doctors.serializers import DoctorSerializer
from patients.serializers import PatientSerializer
from .models import PatientDoctorMapping

class MappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_at']
        read_only_fields = ['id', 'assigned_at']

    def validate_patient(self, value):
        request = self.context.get('request')
        if value.created_by != request.user:
            raise serializers.ValidationError(
                "You can only assign doctors to your own patients."
            )
        return value

    def validate(self, data):
        if PatientDoctorMapping.objects.filter(
            patient=data['patient'],
            doctor=data['doctor'],
        ).exists():
            raise serializers.ValidationError(
                "This doctor is already assigned to this patient."
            )
        return data

class MappingDetailSerializer(serializers.ModelSerializer):

    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_at']