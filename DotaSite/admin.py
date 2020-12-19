from django.contrib import admin
from.models import DotaUser,DotaAdmin,DotaGamer,DotaPremiumuser,DotaMmr,DotaTournament,DotaGamerMatchTournament,DotaMatch
# Register your models here.
admin.site.register(DotaUser)
admin.site.register(DotaAdmin)
admin.site.register(DotaGamer)
admin.site.register(DotaPremiumuser)
admin.site.register(DotaMmr)
admin.site.register(DotaTournament)
admin.site.register(DotaGamerMatchTournament)
admin.site.register(DotaMatch)