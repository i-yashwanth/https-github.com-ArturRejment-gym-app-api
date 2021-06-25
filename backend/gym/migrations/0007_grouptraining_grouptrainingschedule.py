# Generated by Django 3.2.4 on 2021-06-25 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_receptionist_shop'),
        ('gym', '0006_shopproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupTraining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=250)),
                ('max_people', models.IntegerField()),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.workinghours')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='GroupTrainingSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.grouptraining')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.gymmember')),
            ],
        ),
    ]
