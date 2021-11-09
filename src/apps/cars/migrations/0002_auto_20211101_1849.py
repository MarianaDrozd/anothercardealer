# Generated by Django 3.1.7 on 2021-11-01 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dealers.dealer'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.model'),
        ),
        migrations.AddField(
            model_name='car',
            name='picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cars.picture'),
        ),
    ]
