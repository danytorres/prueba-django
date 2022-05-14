from django.db import models

# Create your models here.
class Municipio(models.Model):
    clave = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)


class Estado(models.Model):
    clave = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)


class Colonia(models.Model):
    clave = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)


class TipoAsentamiento(models.Model):
    clave = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)


class Ciudad(models.Model):
    clave = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)


class Zona(models.Model):
    nombre = models.CharField(max_length=255)


class CodigoPostal(models.Model):
    codigo_postal = models.IntegerField()
    colonia = models.ForeignKey(Colonia, on_delete=models.SET_NULL, null=True)
    tipo_asentamiento = models.ForeignKey(TipoAsentamiento, on_delete=models.SET_NULL, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    codigo_reparte = models.IntegerField()
    zona = models.ForeignKey(Zona, on_delete=models.SET_NULL, null=True)

