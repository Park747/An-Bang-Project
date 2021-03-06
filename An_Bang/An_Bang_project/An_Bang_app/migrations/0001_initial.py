# Generated by Django 4.0.4 on 2022-04-17 10:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('cctv', models.BooleanField(default=False)),
                ('entrance', models.BooleanField(default=False)),
                ('guard', models.BooleanField(default=False)),
                ('elevator', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('uploaded', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=1)),
                ('birth_year', models.IntegerField()),
                ('birth_month', models.IntegerField()),
                ('birth_date', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('is_student', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo', models.TextField()),
                ('uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.IntegerField(default=0)),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.building')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.profile')),
            ],
            options={
                'ordering': ['uploaded'],
                'unique_together': {('user_id', 'building_id')},
            },
        ),
        migrations.CreateModel(
            name='Recomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('uploaded', models.DateField(default=django.utils.timezone.now)),
                ('target_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.comment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('soundproof', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('safety', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('water_pressure', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('new', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('lighting', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('insect', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.review')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.review'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.profile'),
        ),
        migrations.CreateModel(
            name='Save',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.building')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='An_Bang_app.profile')),
            ],
            options={
                'unique_together': {('user_id', 'building_id')},
            },
        ),
    ]
