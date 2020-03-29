from rest_framework import serializers
from .models import Barangay, CaseBulletin, Case


class BarangaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Barangay
        fields = ['id', 'name', 'latitude', 'longitude']


class CaseSerializer(serializers.ModelSerializer):
    barangay = BarangaySerializer(read_only=True)

    class Meta:
        model = Case
        fields = ['id', 'case_bulletin', 'barangay', 'pui', 'pum']


class CaseBulletinSerializer(serializers.ModelSerializer):
    cases = CaseSerializer(many=True, read_only=True)

    class Meta:
        model = CaseBulletin
        fields = ['id', 'log_time', 'pum_total', 'pum_completed', 'pum_cleared', 'pum_ongoing', 'pui_total',
                  'pui_admitted', 'pui_completed', 'pui_home', 'pui_cleared', 'cases']


class DailyCaseBulletinSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseBulletin
        fields = ['id', 'log_time', 'pum_total', 'pui_total']
