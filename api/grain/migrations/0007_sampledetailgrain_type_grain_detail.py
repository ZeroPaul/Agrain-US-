# Generated by Django 2.2.4 on 2019-10-15 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grain', '0006_samplegrain_image_recognized_grains'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampledetailgrain',
            name='type_grain_detail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail_type', to='grain.TypeGrain'),
        ),
    ]