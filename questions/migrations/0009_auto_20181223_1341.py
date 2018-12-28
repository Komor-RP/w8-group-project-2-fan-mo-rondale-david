# Generated by Django 2.1.4 on 2018-12-23 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20181223_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resolve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='answer',
            name='resolving_answer',
        ),
        migrations.AddField(
            model_name='question',
            name='resolving_answer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resolved', to='questions.Answer'),
        ),
        migrations.AddField(
            model_name='resolve',
            name='resolved_question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resolved', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='resolve',
            name='valid_answer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resolving', to='questions.Answer'),
        ),
    ]