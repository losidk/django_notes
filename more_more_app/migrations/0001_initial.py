# Generated by Django 3.2.5 on 2022-11-06 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('friends', models.ManyToManyField(related_name='_more_more_app_student_friends_+', to='more_more_app.Student')),
            ],
        ),
    ]