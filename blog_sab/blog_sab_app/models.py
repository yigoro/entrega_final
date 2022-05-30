from django.db import models

class Estudio(models.Model):
    universidad = models.CharField(max_length=40)
    anio_inicio = models.IntegerField()
    titulo = models.CharField(max_length=40)
    finalizado = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.universidad} - Inicio: {self.anio_inicio} - Titulo: {self.titulo} - Finalizado: {self.finalizado}'

class Viajes(models.Model):
    destino = models.CharField(max_length=40)
    nro_vuelo = models.IntegerField()
    fecha = models.DateField()
    notas = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.destino}  - Vuelo: {self.nro_vuelo} - Fecha: {self.fecha} - Notas: {self.notas}'

class Empleos(models.Model):
    empresa = models.CharField(max_length=30)
    periodo = models.IntegerField()
    puesto = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.empresa} - Periodo: {self.periodo} - Puesto: {self.puesto}'
