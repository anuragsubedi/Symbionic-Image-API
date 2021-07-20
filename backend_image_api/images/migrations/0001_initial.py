# Generated by Django 3.2.5 on 2021-07-20 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(default='posts/default.jpg', upload_to=images.models.user_directory_path)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='images.category')),
            ],
        ),
    ]