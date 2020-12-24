from django.shortcuts import render
from .models import DotaTournament
from django.contrib.auth.decorators import login_required
# Create your views here.
from DotaSite.models import DotaUser, DotaPremiumuser ,DotaMmr, DotaMatch, DotaTournament , DotaGamer,DotaGamerMatch,DotaTournamentMatch

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
@login_required
def listmatch(request):
 
    allmatch= DotaGamerMatch.objects.prefetch_related('matchid','gamerid')
    
    context= {'allmatch': allmatch}

        
    return render(request, 'listmatch.html', context=context)

# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return redirect("/")
    else:
	    form = RegisterForm()

    return render(response, "register.html", {"form":form})