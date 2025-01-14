# Generated by Django 2.1.3 on 2019-10-01 23:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customer_submitters_can_create_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusEmailSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify', models.CharField(choices=[('0_NEVER', "Don't notify"), ('1_DAILY', 'Daily')], default='0_NEVER', max_length=255)),
                ('last_notified', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
