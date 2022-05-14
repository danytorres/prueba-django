from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from codigos.models import CodigoPostal
from rest_framework.permissions import AllowAny, IsAuthenticated
from codigos.serializers import CodigoPostalSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class View(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            if request.GET.get('CP'):
                get_codigo = CodigoPostal.objects.filter(codigo_postal=int(request.query_params['CP']))
            elif request.GET.get('colonia'):
                get_codigo = CodigoPostal.objects.filter(colonia__nombre__contains=request.query_params['colonia'])
            elif request.GET.get('municipio'):
                get_codigo = CodigoPostal.objects.filter(municipio__nombre__contains=request.query_params['municipio'])
            elif request.GET.get('estado'):
                get_codigo = CodigoPostal.objects.filter(estado__nombre__contains=request.query_params['estado'])
        except:
            return Response(
                {"message": "Error, no se encontro el documento"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        codigo = CodigoPostalSerializer(get_codigo, many=True)
        return Response(codigo.data, status=status.HTTP_200_OK)