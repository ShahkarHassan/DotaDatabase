# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DotaAdmin(models.Model):
    admin = models.ForeignKey('DotaUser', models.DO_NOTHING, primary_key=True)
    admin_registration_number = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'dota_admin'


class DotaGamer(models.Model):
    gamer = models.ForeignKey('DotaUser', models.DO_NOTHING, primary_key=True)
    gamer_ign = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dota_gamer'


class DotaGamerMatchTournament(models.Model):
    matchid = models.ForeignKey('DotaMatch', models.DO_NOTHING, db_column='matchid', primary_key=True)
    gamerid = models.ForeignKey(DotaGamer, models.DO_NOTHING, db_column='gamerid')
    tournamentid = models.ForeignKey('DotaTournament', models.DO_NOTHING, db_column='tournamentid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dota_gamer_match_tournament'


class DotaMatch(models.Model):
    match_id = models.IntegerField(db_column='match_ID', primary_key=True)  # Field name made lowercase.
    match_status = models.CharField(db_column='match_Status', max_length=15)  # Field name made lowercase.
    match_gpm = models.IntegerField(db_column='match_GPM')  # Field name made lowercase.
    match_kills = models.IntegerField(db_column='match_Kills')  # Field name made lowercase.
    match_xpm = models.IntegerField(db_column='match_XPM')  # Field name made lowercase.
    match_death = models.IntegerField()
    match_assist = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dota_match'


class DotaMmr(models.Model):
    mmr = models.ForeignKey(DotaGamer, models.DO_NOTHING, db_column='mmr_Id', primary_key=True)  # Field name made lowercase.
    mmr_score = models.BigIntegerField()
    mmr_medal = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dota_mmr'


class DotaPremiumuser(models.Model):
    premiumuser_gamer = models.ForeignKey(DotaGamer, models.DO_NOTHING, db_column='premiumuser_Gamer_ID')  # Field name made lowercase.
    premiumuser_registration_number = models.BigIntegerField(db_column='premiumuser_Registration_Number', primary_key=True)  # Field name made lowercase.
    premiumuser_registrationexpirydate = models.CharField(db_column='premiumuser_RegistrationExpiryDate', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dota_premiumuser'


class DotaTournament(models.Model):
    tournament_id = models.IntegerField(db_column='Tournament_ID', primary_key=True)  # Field name made lowercase.
    tournament_name = models.CharField(db_column='Tournament_name', max_length=100)  # Field name made lowercase.
    tournament_starting_timedate = models.DateTimeField(db_column='Tournament_starting_timedate')  # Field name made lowercase.
    tournament_prize = models.IntegerField(db_column='Tournament_prize', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dota_tournament'


class DotaUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=45)
    user_email = models.CharField(max_length=45)
    user_username = models.CharField(unique=True, max_length=30)
    user_password = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dota_user'
