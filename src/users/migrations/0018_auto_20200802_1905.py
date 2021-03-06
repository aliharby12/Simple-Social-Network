# Generated by Django 2.2 on 2020-08-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20200801_1425'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='profile',
        ),
        migrations.AlterField(
            model_name='profile',
            name='Specialist_doctor',
            field=models.CharField(choices=[('امراض دم', 'امراض دم'), ('اطفال', 'اطفال'), ('انف واذن', 'انف واذن'), ('اسنان', 'اسنان'), ('جراحه عامه', 'جراحه عامه'), ('مخ واعصاب', 'مخ واعصاب'), ('جراحه تجميل', 'جراحه تجميل'), ('اورام', 'اورام'), ('جراحه اطفال', 'جراحه اططفال'), ('حميات', 'حميات'), ('نسا وتوليد', 'نسا وتوليد'), ('باطنة', 'باطنه'), ('تخسيس', 'تخسيس'), ('عظام', 'عظام')], default='باطنه', max_length=255, verbose_name='التخصص'),
        ),
    ]
