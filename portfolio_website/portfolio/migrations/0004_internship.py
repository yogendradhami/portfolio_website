# Generated by Django 4.1.7 on 2023-04-02 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_blogs_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('usn', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('college_name', models.CharField(max_length=100)),
                ('offer_status', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=100)),
                ('end_date', models.CharField(max_length=100)),
                ('project_report', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
