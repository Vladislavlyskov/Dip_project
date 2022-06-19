# Generated by Django 4.0.3 on 2022-04-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_customer_contact_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='hobbies',
            field=models.ManyToManyField(related_name='persons', to='main_app.hobbies'),
        ),
    ]
