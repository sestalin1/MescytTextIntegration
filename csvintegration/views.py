from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import psycopg2
import logging

def index(request):
	data = {}
	if "GET" == request.method:
		return render(request, "index.html", data)

	try:
		csv_file = request.FILES["csv_file"]
		conn = psycopg2.connect("host=localhost dbname=MescytDB user=postgres password=prueba port=5433")
		cur = conn.cursor()
		#with open(csv_file, 'r') as f:
			# Notice that we don't need the `csv` module.
		#next(csv_file) # Skip the header row.
		cur.copy_from(csv_file, 'csvintegration_carreer', sep=',',columns=['name','university_id','enrollment','graduates','opening_date','closing_date','credits','degree'])
		conn.commit()

	
	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"No se ha podido cargar el archivo. "+repr(e))

	return HttpResponseRedirect(reverse("index"))