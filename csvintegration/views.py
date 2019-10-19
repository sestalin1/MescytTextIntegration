from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import psycopg2
import logging
import sys
#import pandas as pd
import csv
from .models import Carreer

def index(request):
	data = {}
	if "GET" == request.method:
		return render(request, "index.html", data)

	
	try:
		conn = psycopg2.connect("host=localhost dbname=MescytDB user=postgres password=prueba port=5433")
		cur = conn.cursor()
		
		csv_file = request.FILES["csv_file"]
		cur.copy_from(csv_file, 'csvintegration_carreer', sep=',',columns=['name','university_id','enrollment','graduates','opening_date','closing_date','credits','degree'])
		conn.commit()

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"No se ha podido cargar el archivo. "+repr(e))

	return HttpResponseRedirect(reverse("index"))


def toCSV(request):
	model_class = Carreer
	
	meta = model_class._meta
	field_names = ['name',
		'university_id',
		'enrollment',
		'graduates',
		'opening_date',
		'closing_date',
		'credits','degree'
		]
	
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=CarrerasMescyt.csv'.format(meta)
	writer = csv.writer(response)

	writer.writerow(field_names)
	for obj in model_class.objects.all():
		row = writer.writerow([getattr(obj, field) for field in field_names])

	return response