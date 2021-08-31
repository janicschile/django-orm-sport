from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
    
	ligasBeisbol = League.objects.filter(sport='Baseball')
	ligasMujer = League.objects.filter(name__contains="Women")
	deporteHockey = League.objects.filter(sport__contains="Hockey")
	noFootball = League.objects.exclude(sport="Football")
	nombreConferencia = League.objects.filter(name__contains="Conference")
	regionAtlanta = Team.objects.filter(location__contains="Atlanta")
	sedeDalla = Team.objects.filter(location__contains="Dallas")
	losRaptor = Team.objects.filter(team_name__contains="Raptors")
	existeCity = Team.objects.filter(location__contains="city")
	comienzaConT = Team.objects.filter(team_name__startswith="T")
	porUbicacion = Team.objects.all().order_by("location")
	porEquipoInverso = Team.objects.all().order_by("-team_name")
	apellidoCooper = Player.objects.filter(last_name="Cooper")
	nombreJoshua = Player.objects.filter(first_name="Joshua")
	#apellidoCooperSinJoshua = Player.objects.filter(last_name="Cooper")
	apellidoCooperSinJoshua = Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
	soloDosNombre = Player.objects.filter(first_name__in=("Alexander", "Wyatt")).order_by("first_name")

	print(soloDosNombre)
	for a in soloDosNombre:
		print(f"{a.first_name} - {a.last_name}")


	context = {
		"ligasBeisbols": ligasBeisbol,
		"ligasMujeres": ligasMujer,
		"deporteHockeys": deporteHockey,
		"noFootballs": noFootball,
		"nombreConferencias": nombreConferencia,
		"regionAtlantas": regionAtlanta,
		"sedeDallas": sedeDalla,
		"losRaptors": losRaptor,
		"existeCitys": existeCity,
		"comienzaConTs": comienzaConT,
		"porUbicacions": porUbicacion,
		"porEquipoInversos": porEquipoInverso,
		"apellidoCoopers": apellidoCooper,
		"nombreJoshuas": nombreJoshua,
		"apellidoCooperSinJoshuas": apellidoCooperSinJoshua,
		"soloDosNombres": soloDosNombre,
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")