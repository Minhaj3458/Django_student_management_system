# Generated by Django 3.2.3 on 2021-07-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0004_online_apply_trimester'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddCourse',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Course_Name', models.CharField(max_length=255)),
                ('Course_Code', models.CharField(max_length=255)),
                ('Start_Date', models.CharField(max_length=255)),
                ('Course_Duration', models.CharField(max_length=255)),
                ('Course_Price', models.CharField(max_length=255)),
                ('Batch', models.CharField(max_length=255)),
                ('Trimester', models.CharField(max_length=255)),
                ('Professor_Name', models.CharField(max_length=255)),
                ('Contact_Number', models.IntegerField()),
                ('Course_Photo', models.ImageField(upload_to='')),
                ('Course_Details', models.CharField(max_length=500)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'AddCourses',
            },
        ),
    ]
