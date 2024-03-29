# Generated by Django 3.1.6 on 2021-06-01 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Productsenderaddress', models.CharField(max_length=200, null=True)),
                ('cotumer_address', models.CharField(max_length=200, null=True)),
                ('zipbnumber', models.CharField(max_length=200)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('disability', models.CharField(choices=[('Psychosocial Disability', 'psychosocial disability'), ('Chronic Illness', 'chronic illness'), ('Learning Disability', 'learning disability'), ('Mental Disability', 'mental disability'), ('Visual Disability', 'visual disability'), ('Orthopedic Disability', 'orthopedic disability'), ('Communication Disability', 'communication disability')], max_length=200)),
                ('address', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(max_length=200, null=True)),
                ('Cnum', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('Idpic', models.FileField(upload_to='static/')),
            ],
        ),
        migrations.CreateModel(
            name='BAYAD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(choices=[('Online', 'online'), ('Cash On Delivery', 'Cod')], max_length=50)),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemVariant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('attachment', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencecode', models.CharField(blank=True, max_length=100, null=True)),
                ('datestart', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('Item_being_ready_fo_pick', models.BooleanField(default=False)),
                ('tobedelivered', models.BooleanField(default=False)),
                ('Order_received', models.BooleanField(default=False)),
                ('refund_request', models.BooleanField(default=False)),
                ('refund_approved', models.BooleanField(default=False)),
                ('costumer_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='costumer_address', to='FORPWD.address')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FORPWD.coupon')),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discountedprice', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Eye Wear', 'eye wear'), ('Wheelchairs', 'wheelchairs'), ('Hearingaids', 'hearingaids'), ('Crutches', 'crutches'), ('Tactiles', 'tactiles')], max_length=100)),
                ('slugtourl', models.SlugField(max_length=200)),
                ('itemdescription', models.TextField()),
                ('itemImage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FORPWD.productitem')),
            ],
            options={
                'unique_together': {('item', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_issue', models.CharField(choices=[('Damaged', 'damaged'), ('Defective', 'defective'), ('Wrong Item', 'wrong item')], max_length=200, null=True)),
                ('reason_description', models.TextField()),
                ('imageevidence', models.ImageField(null=True, upload_to='')),
                ('accepted', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FORPWD.orderdetails')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FORPWD.productitem')),
                ('item_variations', models.ManyToManyField(to='FORPWD.ItemVariant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='itemwiths',
            field=models.ManyToManyField(to='FORPWD.OrderItem'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='FORPWD.bayad'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='sender_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender_address', to='FORPWD.address'),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemvariant',
            name='variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FORPWD.variants'),
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discuss', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('url', models.ImageField(blank=True, upload_to='static/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FORPWD.discussion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('birthdate', models.DateField()),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FORPWD.applicant')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='itemvariant',
            unique_together={('variation', 'value')},
        ),
    ]
