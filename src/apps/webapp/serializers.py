from rest_framework import serializers
from .models import Barangay, CaseBulletin, Case, BarangayHotline, TimeLineEntry


class BarangayHotlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarangayHotline
        fields = ['id', 'contact_number']


class BarangaySerializer(serializers.ModelSerializer):
    barangay_hotline = BarangayHotlineSerializer(many=True, read_only=True)

    class Meta:
        model = Barangay
        fields = ['id', 'name', 'latitude', 'longitude', 'barangay_hotline']


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
        fields = ['id', 'log_time', 'pum_total', 'pum_completed', 'pum_cleared', 'pum_ongoing', 'pui_total',
                  'pui_admitted', 'pui_completed', 'pui_home', 'pui_cleared']


class TimeLineEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = TimeLineEntry
        fields = ['id', 'title', 'entry_timestamp', 'text', 'details_link']
