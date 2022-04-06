# Generated by Django 4.0.3 on 2022-04-02 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0005_alter_commentticket_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentticket',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='support.commentticket', verbose_name='Родитель'),
        ),
        migrations.AlterField(
            model_name='commentticket',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.ticket', verbose_name='Тикет'),
        ),
    ]