from django.shortcuts import render
import sys
import os
from View import DataCollection
from View.DataCollection import pop_density
from . import voronoi
import simplejson
import io
import urllib, base64
import os.path
import json
BASE = os.path.dirname(os.path.abspath(__file__))

# os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DataCollection', 'jp.csv')

# Create your views here.

def main_page(request):
	opt = pop_density.get_optimal_distribution()
	f = open(os.path.join(BASE, "json_gradovi.json"), )
	data = json.load(f)
	ll1=[]
	for i, x in enumerate(opt):
		ll1.append(str(x[0]))
		ll1.append(str(x[1]))
	json_list = simplejson.dumps(ll1)
	return render(request, 'home.html', {'data2': json_list, 'tabela': data})


def voronoi_prikaz(request):
	figura = voronoi.voronoi_funkcija()
	buf = io.BytesIO()
	figura.savefig(buf, format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri = urllib.parse.quote(string)
	return render(request, 'voronoi.html')

	
def unesi_koordinatu(request):
	if request.method == 'POST':
		print(request.POST)
		
	koords = [int(request.POST['xkoord']), int(request.POST['ykoord'])]
	print(koords)
	figura = voronoi.voronoi_funkcija(koords)
	buf = io.BytesIO()
	figura.savefig(buf, format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri = urllib.parse.quote(string)
	return render(request, 'voronoi.html', {'pic': uri})