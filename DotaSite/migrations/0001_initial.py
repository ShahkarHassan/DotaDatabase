# Generated by Django 2.1.15 on 2020-12-18 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DotaMatch',
            fields=[
                ('match_id', models.IntegerField(db_column='match_ID', primary_key=True, serialize=False)),
                ('match_status', models.CharField(db_column='match_Status', max_length=15)),
                ('match_gpm', models.IntegerField(db_column='match_GPM')),
                ('match_kills', models.IntegerField(db_column='match_Kills')),
                ('match_xpm', models.IntegerField(db_column='match_XPM')),
                ('match_death', models.IntegerField()),
                ('match_assist', models.IntegerField()),
            ],
            options={
                'db_table': 'dota_match',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DotaPremiumuser',
            fields=[
                ('premiumuser_registration_number', models.BigIntegerField(db_column='premiumuser_Registration_Number', primary_key=True, serialize=False)),
                ('premiumuser_registrationexpirydate', models.CharField(db_column='premiumuser_RegistrationExpiryDate', max_length=30)),
            ],
            options={
                'db_table': 'dota_premiumuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DotaTournament',
            fields=[
                ('tournament_id', models.IntegerField(db_column='Tournament_ID', primary_key=True, serialize=False)),
                ('tournament_name', models.CharField(db_column='Tournament_name', max_length=100)),
                ('tournament_starting_timedate', models.DateTimeField(db_column='Tournament_starting_timedate')),
                ('tournament_prize', models.IntegerField(blank=True, db_column='Tournament_prize', null=True)),
            ],
            options={
                'db_table': 'dota_tournament',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DotaUser',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=45)),
                ('user_email', models.CharField(max_length=45)),
                ('user_username', models.CharField(max_length=30, unique=True)),
                ('user_password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'dota_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dota_Admin',
            fields=[
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DotaSite.DotaUser')),
                ('admin_registration_number', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'dota_admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DotaGamer',
            fields=[
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DotaSite.DotaUser')),
                ('gamer_ign', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'dota_gamer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DotaGamerMatchTournament',
            fields=[
                ('matchid', models.ForeignKey(db_column='matchid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DotaSite.DotaMatch')),
            ],
            options={
                'db_table': 'dota_gamer_match_tournament',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DotaMmr',
            fields=[
                ('mmr', models.ForeignKey(db_column='mmr_Id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DotaSite.DotaGamer')),
                ('mmr_score', models.BigIntegerField()),
                ('mmr_medal', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'dota_mmr',
                'managed': False,
            },
        ),
    ]
