from django.db import models


class University(models.Model):
	rnc = models.IntegerField('RNC')
	name = models.CharField('Nombre',max_length = 50)


class Carreer(models.Model):
	name = models.CharField('Nombre',max_length = 50)
	univesity = models.ForeignKey(University, related_name = 'UniversityCarrersFK',on_delete = models.CASCADE, default = '')
	enrollment = models.IntegerField('Inscritos', default = 0)
	graduates = models.IntegerField('Graduados', default = 0)
	openingDate = models.DateField('Fecha de Apertura', blank=True, null=True)
	closingDate = models.DateField('Fecha de Cierre',blank=True,null=True)
	credits = models.IntegerField('Creditos',default = 0)
	
	degrees = (
		('undergraduate','Grado'),
		('graduate','Postgrado'),
	)
	degree = models.CharField('Nivel',max_length = 13, choices = degrees, null=True)
"""		universities = models.ManyToManyField(University, db_table = 'UnivesitiesCarreers')
	

class UnivesitiesCarreers(models.Model):
	univesity = models.ForeignKey(University, on_delete = models.CASCADE)
	carreer = models.ForeignKey(Carreer, on_delete = models.CASCADE)
	enrollment = models.IntegerField('Inscritos')
	graduates = models.IntegerField('Graduados')
	openingDate = models.DateField('Fecha de Apertura')
	closingDate = models.DateField('Fecha de Cierre')
	credits = models.IntegerField('Creditos')
	
	degrees = (
		('undergraduate','Grado'),
		('graduate','Postgrado'),
	)
	degree = models.CharField('Nivel',max_length = 13, choices = degrees)
	
"""