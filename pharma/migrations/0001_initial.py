from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='med',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medName', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=3, decimal_places=2)),
                ('quantity', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
