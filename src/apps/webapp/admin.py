from django.contrib import admin
from .models import Barangay, CaseBulletin, Case, BarangayHotline, TimeLineEntry

admin.site.site_header = 'MC COVID-19 Admin Panel'
admin.site.site_title = 'Malaybaylay City COVID-19 Dashboard'
admin.site.index_title = 'Malaybaylay City COVID-19 Dashboard'


class BarangayAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name', 'latitude', 'longitude']


class BarangayHotlineAdmin(admin.ModelAdmin):
    list_display = ['barangay', 'contact_number']


class CaseAdmin(admin.ModelAdmin):
    list_display = ['barangay', 'case_bulletin', 'pum', 'pui']


class CaseInline(admin.TabularInline):
    model = Case


class CaseBulletinAdmin(admin.ModelAdmin):
    list_display = ['log_time', 'pum_total', 'pui_total']
    inlines = [CaseInline]


class TimeLineEntryAdmin(admin.ModelAdmin):
    ordering = ['-entry_timestamp']
    list_display = ['title', 'entry_timestamp']


admin.site.register(Barangay, BarangayAdmin)
admin.site.register(CaseBulletin, CaseBulletinAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(BarangayHotline, BarangayHotlineAdmin)
admin.site.register(TimeLineEntry, TimeLineEntryAdmin)
