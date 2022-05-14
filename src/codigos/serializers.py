from rest_framework import serializers
from codigos.models import Municipio, Estado, Colonia, TipoAsentamiento, Ciudad, Zona, CodigoPostal

class CodigoPostalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodigoPostal
        fields = "__all__"
        depth = 1
