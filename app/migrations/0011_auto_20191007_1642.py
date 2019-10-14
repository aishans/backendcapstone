# Generated by Django 2.2.6 on 2019-10-07 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_question_question_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answers',
            new_name='is_correct',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_subject',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.CharField(max_length=120),
        ),
    ]
