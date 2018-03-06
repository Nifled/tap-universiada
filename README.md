# TAP-Universiada

### Run locally

Para correr localmente se debe tener `docker`/`docker-compose`, o puedes instalar y configurar todo manualmente (no recomendable).

```shell
$ docker-compose -f compose-local.yml build

# run it
$ docker-compose -f compose-local.yml up
```

Para correr comandos de Django como `migrate` o `createsuperuser`, se hace a travez de `docker-compose`:

```shell
$ docker-compose -f compose-local.yml run web python manage.py migrate
$ docker-compose -f compose-local.yml run web python manage.py createsuperuser
```