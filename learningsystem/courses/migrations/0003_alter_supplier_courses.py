# Generated by Django 4.1 on 2022-10-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_skill_id_course_alter_supplier_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='courses',
            field=models.ManyToManyField(blank=True, default=None, to='courses.course'),
        ),
    ]