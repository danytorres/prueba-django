# API SEPOMEX

Api empaquetado en docker file y compuesto con docker-compose, creando un contenedor empaquetando el proyecto django y conectandose con otro contenedor con postgresql

Al momento de crear los contenedores se carga de inmediato un comando especial seedscript para cargar los datos en la base de datos, si detecta que ya tiene datos,se pasa este paso y activa el servidor con gunicorn con 5 workers

## Funcionamiento

El api de busqueda funciona con el siguiente link:

```
/api/?CP={codigo postal a buscar}

/api/?colonia={colonia a buscar}

/api/?municipio={municipio a buscar}

/api/?estado={estado a buscar}
```

## Autenticacion

La autenticacion es por medio de un Token que se tiene que poner en los headers:

```
Authorization: Token {Token}
```

Para obtener el token se tiene que tener un usuario Django y entrar a el siguiente link:

```
/api-token-auth/
```

Con el metodo POST con con los siguientes datos del usuario:

```
username

password
```

se necesita entrar a la pagina de administracion de Django para crear un nuevo usuario

## Variables de entorno

las variables de entorno dentro de docker compose son las siguientespara crear el super usuario

      - DJANGO_SUPERUSER_USERNAME=
      - DJANGO_SUPERUSER_PASSWORD=
      - DJANGO_SUPERUSER_EMAIL=

Al momento de empezar se verifica si ya se tiene este super usuario y si no se crea.

