# Generated by Django 3.0.4 on 2020-03-26 22:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CaseBulletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('pum_total', models.IntegerField(default=0)),
                ('pum_completed', models.IntegerField(default=0)),
                ('pum_cleared', models.IntegerField(default=0)),
                ('pum_ongoing', models.IntegerField(default=0)),
                ('pui_total', models.IntegerField(default=0)),
                ('pui_admitted', models.IntegerField(default=0)),
                ('pui_completed', models.IntegerField(default=0)),
                ('pui_home', models.IntegerField(default=0)),
                ('pui_cleared', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pui', models.IntegerField()),
                ('pum', models.IntegerField()),
                ('barangay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='webapp.Barangay')),
                ('case_bulletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to='webapp.CaseBulletin')),
            ],
        ),
    ]
