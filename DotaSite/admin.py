from django.contrib import admin
from.models import DotaUser,DotaAdmin,DotaGamer,DotaPremiumuser,DotaMmr,DotaTournament,DotaGamerMatch,DotaMatch,DotaTournamentMatch
# Register your models here.
admin.site.register(DotaUser)
admin.site.register(DotaAdmin)
admin.site.register(DotaGamer)
admin.site.register(DotaPremiumuser)
admin.site.register(DotaMmr)
admin.site.register(DotaTournament)
admin.site.register(DotaGamerMatch)
admin.site.register(DotaMatch)
admin.site.register(DotaTournamentMatch)
