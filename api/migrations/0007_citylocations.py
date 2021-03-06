# Generated by Django 3.2.7 on 2021-12-08 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_delete_citylocations'),
    ]

    operations = [
        migrations.CreateModel(
            name='cityLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('communitiny', models.CharField(blank=True, max_length=100)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.city')),
            ],
        ),
    ]
