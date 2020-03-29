from django.contrib import admin
from .models import Barangay, CaseBulletin, Case

admin.site.site_header = 'MC COVID-19 Admin Panel'
admin.site.site_title = 'Malaybaylay City COVID-19 Dashboard'
admin.site.index_title = 'Malaybaylay City COVID-19 Dashboard'


class BarangayAdmin(admin.ModelAdmin):
    list_display = ['name', 'latitude', 'longitude']


class CaseAdmin(admin.ModelAdmin):
    list_display = ['barangay', 'case_bulletin', 'pum', 'pui']


class CaseInline(admin.TabularInline):
    model = Case


class CaseBulletinAdmin(admin.ModelAdmin):
    list_display = ['log_time', 'pum_total', 'pui_total']
    inlines = [CaseInline]


admin.site.register(Barangay, BarangayAdmin)
admin.site.register(CaseBulletin, CaseBulletinAdmin)
admin.site.register(Case, CaseAdmin)
