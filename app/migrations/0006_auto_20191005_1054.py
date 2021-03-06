# Generated by Django 2.2.6 on 2019-10-05 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191005_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=120)),
                ('teacher_name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='classification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.School'),
        ),
    ]
