# Generated by Django 4.0.1 on 2022-01-23 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Screed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('A', 'Attack'), ('D', 'Defense'), ('S', 'Support')], default='S', max_length=1)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField(default=0)),
                ('power', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='type',
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Screed.traveler'),
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='score',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='node',
            name='title',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='reward',
            name='choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Screed.choice'),
        ),
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='edit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('text', models.TextField()),
                ('positive', models.IntegerField(default=1)),
                ('negative', models.IntegerField(default=1)),
                ('author', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Screed.user')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='item_definition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Screed.itemdefinition'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Screed.itemdefinition'),
        ),
    ]
