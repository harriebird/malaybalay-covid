from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import BarangaySerializer, CaseBulletinSerializer, CaseSerializer, DailyCaseBulletinSerializer
from .models import Barangay, CaseBulletin, Case


def index(request):
    return render(request, 'webapp/index.html')


class BarangayAPIView(generics.ListAPIView):
    queryset = Barangay.objects.all()
    serializer_class = BarangaySerializer


class CaseBulletinAPIView(generics.ListAPIView):
    queryset = CaseBulletin.objects.all()
    serializer_class = CaseBulletinSerializer


class LatestBulletinAPIView(generics.RetrieveAPIView):
    queryset = CaseBulletin.objects.all()
    serializer_class = CaseBulletinSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.latest('log_time')
        return obj


class CaseAPIView(generics.ListAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer


class DailyCaseBulletinAPIView(generics.ListAPIView):
    queryset = CaseBulletin.objects.all()
    serializer_class = DailyCaseBulletinSerializer
