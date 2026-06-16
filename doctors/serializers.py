from rest_framework import serializers

from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source='created_by.email')

    class Meta:
        model = Doctor
        fields = [
            'id', 'created_by', 'name', 'specialization',
            'phone', 'email', 'qualification', 'experience_years',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_by', 'created_at', 'updated_at']