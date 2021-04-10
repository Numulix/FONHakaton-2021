from django.shortcuts import render
import sys
import os
from View import DataCollection
from View.DataCollection import pop_density

# os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DataCollection', 'jp.csv')

# Create your views here.

def main_page(request):
	opt = pop_density.get_optimal_distribution()
	print(opt)
	return render(request, 'home.html', {'data'})