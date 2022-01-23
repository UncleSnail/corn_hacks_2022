# Generated by Django 4.0.1 on 2022-01-23 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Screed', '0004_itemdefinition_authors_statdefinition_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_check',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='Screed.check'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='choice', to='Screed.node'),
        ),
    ]