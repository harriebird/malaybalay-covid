from django.db import models
from django.utils import timezone


class Barangay(models.Model):
    name = models.CharField(max_length=80)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class CaseBulletin(models.Model):
    log_time = models.DateTimeField(default=timezone.now)
    pum_total = models.IntegerField(default=0)
    pum_completed = models.IntegerField(default=0)
    pum_cleared = models.IntegerField(default=0)
    pum_ongoing = models.IntegerField(default=0)
    pui_total = models.IntegerField(default=0)
    pui_admitted = models.IntegerField(default=0)
    pui_completed = models.IntegerField(default=0)
    pui_home = models.IntegerField(default=0)
    pui_cleared = models.IntegerField(default=0)

    def __str__(self):
        return str(self.log_time)


class Case(models.Model):
    case_bulletin = models.ForeignKey(CaseBulletin, related_name='cases',  on_delete=models.CASCADE)
    barangay = models.ForeignKey(Barangay, related_name='cases', on_delete=models.CASCADE)
    pui = models.IntegerField()
    pum = models.IntegerField()

    def __str__(self):
        return '{} @ Barangay {}'.format(self.case_bulletin.log_time, self.barangay.name)
