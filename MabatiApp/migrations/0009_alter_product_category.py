# Generated by Django 4.0 on 2024-12-05 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MabatiApp', '0008_remove_product_coating_remove_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('all', 'All'), ('roofing_sheets', 'Roofing Sheets'), ('gutters_drainage', 'Gutters and Drainage'), ('accessories', 'Accessories'), ('tools_hardware', 'Tools and Hardware')], default='all', max_length=50),
        ),
    ]
