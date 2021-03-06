# Generated by Django 3.0.3 on 2020-03-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='remark',
            field=models.CharField(default='remark', max_length=100, null=True),
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
