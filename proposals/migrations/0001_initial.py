# Generated by Django 4.2.13 on 2024-11-20 07:43

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
            name='ProposalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('max_duration_minutes', models.SmallIntegerField(blank=True, null=True)),
                ('max_duration_hours', models.SmallIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('private_notes', models.TextField(blank=True, null=True)),
                ('additional_speaker_emails', models.CharField(blank=True, max_length=256, null=True)),
                ('audience_level', models.CharField(choices=[('b', 'Beginner - just starting'), ('i', 'Intermediate'), ('a', 'Advanced'), ('n', 'Non technical talk')])),
                ('accessibility_requests', models.TextField(blank=True, null=True)),
                ('proposal_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proposals.proposaltype')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='proposals.track')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
