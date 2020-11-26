# Generated by Django 3.1.2 on 2020-11-02 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20201016_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]