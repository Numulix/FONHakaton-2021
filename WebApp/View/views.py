from django.shortcuts import render
import sys
import os
from View import DataCollection
from View.DataCollection import pop_density
import simplejson

# os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DataCollection', 'jp.csv')

# Create your views here.

def main_page(request):
	opt = pop_density.get_optimal_distribution()
	ll1=[]
	for i, x in enumerate(opt):
		ll1.append(str(x[0]))
		ll1.append(str(x[1]))
	json_list = simplejson.dumps(ll1)
	return render(request, 'home.html', {'data2': json_list})