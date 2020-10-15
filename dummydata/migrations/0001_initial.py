# Generated by Django 2.1.3 on 2019-02-18 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appaccounts', '0012_auto_20190214_2346'),
        ('accounts', '0003_auto_20190124_1825'),
        ('feedback', '0015_auto_20190214_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('app_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appaccounts.AppCompany')),
                ('app_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appaccounts.AppUser')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
                ('feature_request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.FeatureRequest')),
                ('feedback', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Feedback')),
                ('theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feedback.Theme')),
            ],
        ),
    ]