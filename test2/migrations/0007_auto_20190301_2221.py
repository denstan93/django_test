# Generated by Django 2.1.5 on 2019-03-01 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0006_auto_20190131_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.AddField(
            model_name='client',
            name='history',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='raiting',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recording',
            name='name_clieint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Client'),
        ),
        migrations.AddField(
            model_name='recording',
            name='name_master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Master'),
        ),
    ]