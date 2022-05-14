import os
from django.core.management.base import BaseCommand, CommandError
from codigos.models import Municipio, Estado, Colonia, TipoAsentamiento, Ciudad, Zona, CodigoPostal

class Command(BaseCommand):
    help = "Script para rellenar de datos la base de datos" 

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+',type=str)

    def handle(self, *args, **options):
        file = os.getcwd() + "/" + options['file'][0]
        print(file)
        f = open(file, encoding="ISO-8859-1")
        tamano = len(f.readlines())
        f.close()
        with open(file, encoding="ISO-8859-1") as f:
            i = 0
            p = 0
            s = ''
            l = 0
            porcentaje = tamano/100
            gato = tamano/10
            print(f"[{s}] {p}%", end="\r")
            
            for line in f:
                i += 1
                if i == 2 or i == 1: continue
                if i%porcentaje == 0: 
                    p += 1
                    print(f"[{s}] {p}%", end="\r")
                if i%gato == 0: 
                    s += '#'
                    print(f"[{s}] {p}%", end="\r")
                
                line = line.split('|')

                codigo = CodigoPostal.objects.filter(
                    codigo_postal=int(line[0]), 
                    colonia=int(line[7].strip("\n") + line[11].strip("\n") + line[12].strip("\n")))
                if len(codigo) > 1: l += 1
                if l > 100: break

                codigo_postal = CodigoPostal(codigo_postal=int(line[0]), codigo_reparte=int(line[6]))

                clave = int(line[7].strip("\n")) if line[7].strip("\n") != '' else None
                recurso = Estado.objects.filter(clave=clave)
                if len(recurso) == 0 and line[7].strip("\n") != '':
                    recurso = Estado(clave=clave, nombre=line[4])
                    recurso.save()
                elif len(recurso) != 0:
                    recurso = recurso[0]
                else:
                    recurso = None
                setattr(codigo_postal, 'estado', recurso)

                clave = int(line[7].strip("\n") + line[11].strip("\n")) if line[11].strip("\n") != '' else None
                recurso = Municipio.objects.filter(clave=clave)
                if len(recurso) == 0 and line[11].strip("\n") != '':
                    recurso = Municipio(clave=clave, nombre=line[3])
                    recurso.save()
                elif len(recurso) != 0:
                    recurso = recurso[0]
                else:
                    recurso = None
                setattr(codigo_postal, 'municipio', recurso)

                clave = int(line[7].strip("\n") + line[11].strip("\n") + line[12].strip("\n")) if line[12].strip("\n") != '' else None
                recurso = Colonia.objects.filter(clave=clave)
                if len(recurso) == 0 and line[12].strip("\n") != '':
                    recurso = Colonia(clave=clave, nombre=line[1])
                    recurso.save()
                elif len(recurso) != 0:
                    recurso = recurso[0]
                else:
                    recurso = None
                setattr(codigo_postal, 'colonia', recurso)

                clave = int(line[10].strip("\n")) if line[10].strip("\n") != '' else None
                recurso = TipoAsentamiento.objects.filter(clave=clave)
                if len(recurso) == 0 and line[10].strip("\n") != '':
                    recurso = TipoAsentamiento(clave=clave, nombre=line[2])
                    recurso.save()
                elif len(recurso) != 0:
                    recurso = recurso[0]
                else:
                    recurso = None
                setattr(codigo_postal, 'tipo_asentamiento', recurso)

                clave = int(line[7].strip("\n") + line[11].strip("\n") + line[12].strip("\n") + line[14].strip("\n")) if line[14].strip("\n") != '' else None
                recurso = Ciudad.objects.filter(clave=clave)
                if len(recurso) == 0 and line[14].strip("\n") != '':
                    recurso = Ciudad(clave=clave, nombre=line[5])
                    recurso.save()
                elif len(recurso) != 0:
                    recurso = recurso[0]
                else:
                    recurso = None
                setattr(codigo_postal, 'ciudad', recurso)

                zona = Zona.objects.filter(nombre=line[13])
                if len(zona) == 0:
                    zona = Zona(nombre=line[13])
                    zona.save()
                else:
                    zona = zona[0]
                codigo_postal.zona = zona

                codigo_postal.save()
