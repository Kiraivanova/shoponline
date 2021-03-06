# Generated by Django 3.1.7 on 2021-10-19 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0001_initial'),
        ('mainap', '0003_auto_20211019_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.ManyToManyField(blank=True, related_name='features_for_product', to='specs.ProductFeatures'),
        ),
        migrations.DeleteModel(
            name='ProductFeatures',
        ),
        migrations.DeleteModel(
            name='ProductFeatureValidator',
        ),
    ]
