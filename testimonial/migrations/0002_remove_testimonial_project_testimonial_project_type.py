# Generated by Django 4.2.17 on 2025-01-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='project',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='project_type',
            field=models.CharField(blank=True, choices=[('brand_videos', 'Brand Videos'), ('explainer_videos', 'Explainer Videos'), ('photography', 'Photography'), ('social_media_content', 'Social Media Content')], max_length=30, null=True),
        ),
    ]
