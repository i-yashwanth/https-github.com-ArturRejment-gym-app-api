# Generated by Django 3.2.4 on 2021-07-04 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0009_alter_grouptraining_training_name'),
        ('people', '0002_receptionist_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receptionist',
            name='shop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gym.shop'),
        ),
    ]
