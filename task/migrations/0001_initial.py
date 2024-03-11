# Generated by Django 4.2.11 on 2024-03-10 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pro_name', models.CharField(max_length=300, verbose_name='Mahsulot nomi:')),
                ('pro_code', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Mahsulot_nomi_',
            },
        ),
        migrations.CreateModel(
            name='ProMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mat_id', to='category.category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pro_id', to='task.product')),
            ],
            options={
                'verbose_name': 'Xomashyo_Mahsulot_',
            },
        ),
    ]