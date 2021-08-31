from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
    #ORM 1
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
	apellidoCooperSinJoshua = Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua")
	soloDosNombre = Player.objects.filter(first_name__in=("Alexander", "Wyatt")).order_by("first_name")

	#ORM 2
	enUnaLiga = Team.objects.all().filter(league=(League.objects.get(name="Atlantic Soccer Conference").id))
	bostonPenguin = Player.objects.all().filter(all_teams=(Team.objects.get(location="Boston").id))
	todosEnColegioInternacional = Player.objects.all().filter(curr_team=(League.objects.get(name="International Collegiate Baseball Conference").id))
	sinLopez = Player.objects.all().filter(all_teams=League.objects.get(name="American Conference of Amateur Football").id) & Player.objects.filter(last_name__contains = 'Lopez')
	fullJugador = Player.objects.filter(curr_team__league__sport = "Football")
	soloSophia = Player.objects.all() & Player.objects.filter(first_name__contains = "Sophia")
	SoloSophiaLiga = League.objects.filter(teams__curr_players__first_name__contains = "sophia")
	apellidoFlores = Player.objects.filter(last_name="Flores").exclude(curr_team__team_name = "Roughriders")
	SoloSamuel = Team.objects.filter(all_players__first_name = "Samuel") & Team.objects.filter(all_players__last_name = "Evans")
	gatoTigre = Player.objects.filter(all_teams__team_name__contains = "Tiger-Cats")
	noViking = Player.objects.filter(all_teams__team_name__contains = "Vikings").exclude(curr_team__team_name = "Vikings")
	noColts = Team.objects.filter(all_players__first_name__contains = "Jacob" ) & Team.objects.exclude(team_name = "Colts")
	joshuaAtlantic = Player.objects.filter(first_name__contains = "Joshua") & Player.objects.filter(all_teams__league__name = "Atlantic Federation of Amateur Baseball Players")
	### __gt  >> mayor que  ###
	### __gte >> mayor o igual que  ###
	### __lt  >> menor que  ###
	### __lte >> menor o igual que  ###
	masDeDoce = Team.objects.annotate(num_players=Count("all_players")).filter(num_players__gte=12)
	jugadoresTotal = Player.objects.annotate(num_teams=Count("all_teams")).order_by("num_teams")

	print(jugadoresTotal)
	for a in jugadoresTotal:
		print(f"{a.first_name} {a.last_name} - {a.num_teams}")
		#print(f"{a.first_name} {a.last_name}")
		#print(f"{a.name}")
		#print(f"{a.team_name}")
		#print(f"{a.id}")


	context = {
		#ORM 1
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
		"players": Player.objects.all(),

		#ORM 2
		"enUnaLigas": enUnaLiga,
		"bostonPenguins": bostonPenguin,
		"todosEnColegioInternacionals": todosEnColegioInternacional,
		"sinLopezs": sinLopez,
		"fullJugadores": fullJugador,
		"soloSophias": soloSophia,
		"SoloSophiaLigas":SoloSophiaLiga,
		"apellidoFloress": apellidoFlores,
		"SoloSamuels": SoloSamuel,
		"gatoTigres": gatoTigre,
		"noVikings": noViking,
		"noColtss": noColts,
		"joshuaAtlantics": joshuaAtlantic,
		"masDeDoces": masDeDoce,
		"jugadoresTotals": jugadoresTotal,
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")