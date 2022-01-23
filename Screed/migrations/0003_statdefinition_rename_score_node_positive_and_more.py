# Generated by Django 4.0.1 on 2022-01-23 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Screed', '0002_itemdefinition_remove_item_name_remove_item_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='node',
            old_name='score',
            new_name='positive',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='choice',
        ),
        migrations.AddField(
            model_name='node',
            name='negative',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reward',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Screed.node'),
        ),
        migrations.AddField(
            model_name='traveler',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Screed.node'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reached_by', to='Screed.node'),
        ),
        migrations.AlterField(
            model_name='edit',
            name='negative',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='type',
            field=models.CharField(choices=[('A', 'Attack'), ('D', 'Defense'), ('S', 'Support'), ('B', 'Burden')], default='S', max_length=1),
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Screed.traveler')),
                ('stat_definition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Screed.statdefinition')),
            ],
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('success_message', models.TextField()),
                ('failure_message', models.TextField()),
                ('value', models.IntegerField(default=1)),
                ('failure_target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_failure', to='Screed.node')),
                ('item_requirement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Screed.itemdefinition')),
                ('stat_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Screed.statdefinition')),
                ('success_target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_success', to='Screed.node')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_check',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='Screed.check'),
        ),
        migrations.AddField(
            model_name='itemdefinition',
            name='cost_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cost_item', to='Screed.statdefinition'),
        ),
        migrations.AddField(
            model_name='itemdefinition',
            name='power_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='power_item', to='Screed.statdefinition'),
        ),
    ]