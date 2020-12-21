from django.shortcuts import render
from .models import DotaTournament
from django.contrib.auth.decorators import login_required
# Create your views here.
from DotaSite.models import DotaUser, DotaPremiumuser ,DotaMmr, DotaMatch, DotaTournament , DotaGamer,DotaGamerMatch,DotaTournamentMatch
@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_gamers = DotaUser.objects.all().count()
    num_PremiumUser = DotaPremiumuser.objects.all().count()

    # Available books (status = 'a')
    num_matches = DotaMatch.objects.all().count()

    # The 'all()' is implied by default.
    num_tournaments = DotaTournament.objects.count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_gamers': num_gamers,
        'num_PremiumUser': num_PremiumUser,
        'num_matches': num_matches,
        'num_tournaments': num_tournaments,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic
@login_required
def listtournament(request):
 
    alltournaments= DotaTournament.objects.all()
    
    context= {'alltournaments': alltournaments}

        
    return render(request, 'listtournament.html', context=context)
@login_required
def listgamermmr(request):
 
    allmmrs = DotaMmr.objects.select_related('mmr')
    context= {'allmmrs':allmmrs}

        
    return render(request, 'listgamermmr.html', context=context)

def listmatch(request):
 
    allmatch= DotaMatch.objects.all()
    
    context= {'allmatch': allmatch}

        
    return render(request, 'listmatch.html', context=context)

def listMMR(request):
 
    allMMR= DotaMmr.objects.all()
    
    context= {'allMMR': allMMR}

        
    return render(request, 'listMMR.html', context=context)
def listtam(request):
 
    alltam= DotaGamerMatchTournament.objects.all()
    
    context= {'alltam': alltam}

        
    return render(request, 'listtam.html', context=context)
def listuser(request):
 
    alluser= DotaUser.objects.all()
    
    context= {'alluser': alluser}

        
    return render(request, 'listuser.html', context=context)
def listpuser(request):
 
    allpuser= DotaPremiumuser.objects.all()
    
    context= {'allpuser': allpuser}

        
    return render(request, 'listpuser.html', context=context)