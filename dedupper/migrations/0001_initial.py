# Generated by Django 2.0.5 on 2018-06-14 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CRD', models.BigIntegerField(blank=True, unique=True)),
                ('firstName', models.CharField(max_length=128)),
                ('lastName', models.CharField(max_length=128)),
                ('suffix', models.CharField(max_length=128)),
                ('canSellDate', models.DateField()),
                ('levelGroup', models.CharField(max_length=128)),
                ('mailingStreet', models.CharField(max_length=128)),
                ('mailingCity', models.CharField(max_length=128)),
                ('mailingStateProvince', models.CharField(max_length=128)),
                ('mailingZipPostalCode', models.IntegerField(blank=True)),
                ('territory', models.CharField(max_length=128)),
                ('workPhone', models.CharField(max_length=128)),
                ('homePhone', models.CharField(max_length=128)),
                ('mobilePhone', models.CharField(max_length=128)),
                ('workEmail', models.CharField(max_length=128)),
                ('personalEmail', models.CharField(max_length=128)),
                ('otherEmail', models.CharField(max_length=128)),
                ('area', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('regionalLeader', models.CharField(max_length=128)),
                ('levelLeader', models.CharField(max_length=128)),
                ('fieldTrainerLeader', models.CharField(max_length=128)),
                ('performanceLeader', models.CharField(max_length=128)),
                ('boaName', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Simple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('author', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('average', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Undecided', 'Undecided'), ('Duplicate', 'Duplicate'), ('New Record', 'New Record')], default='Undecided', max_length=128)),
                ('closest1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='the_closest', to='dedupper.Simple')),
                ('closest2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_closest', to='dedupper.Simple')),
                ('closest3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_closest', to='dedupper.Simple')),
            ],
        ),
        migrations.CreateModel(
            name='RepContact',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dedupper.Contact')),
                ('average', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Undecided', 'Undecided'), ('Duplicate', 'Duplicate'), ('New Record', 'New Record')], default='Undecided', max_length=128)),
                ('dupFlag', models.BooleanField(default=False)),
            ],
            bases=('dedupper.contact',),
        ),
        migrations.CreateModel(
            name='SFContact',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='dedupper.Contact')),
                ('dupFlag', models.BooleanField(default=False)),
                ('closest_rep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='the_closest', to='dedupper.RepContact')),
            ],
            bases=('dedupper.contact',),
        ),
        migrations.AddField(
            model_name='repcontact',
            name='closest1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='the_closest', to='dedupper.SFContact'),
        ),
        migrations.AddField(
            model_name='repcontact',
            name='closest2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_closest', to='dedupper.SFContact'),
        ),
        migrations.AddField(
            model_name='repcontact',
            name='closest3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_closest', to='dedupper.SFContact'),
        ),
    ]
