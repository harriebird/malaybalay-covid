from django.db import models
from django.utils import timezone


class Barangay(models.Model):
    name = models.CharField(max_length=80)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return self.name


class BarangayHotline(models.Model):
    barangay = models.ForeignKey(Barangay, related_name='barangay_hotline', on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.contact_number


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
    pui = models.IntegerField(default=0)
    pum = models.IntegerField(default=0)

    def __str__(self):
        return '{} @ Barangay {}'.format(self.case_bulletin.log_time, self.barangay.name)


class TimeLineEntry(models.Model):
    entry_timestamp = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=300, default='')
    text = models.TextField(default='')
    details_link = models.URLField(max_length=300, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Timeline Entries'
