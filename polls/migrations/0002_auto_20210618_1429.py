# Generated by Django 3.2.4 on 2021-06-18 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='branchs',
        ),
        migrations.AddField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course', to='polls.course'),
        ),
    ]