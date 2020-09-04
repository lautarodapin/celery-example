# Celery beat
```s
$ celery -A CeleryTest beat -l debug --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

# Celery
```s
$ celery -A CeleryTest worker -l debug
```
##### Celery 4 no es soportado por windows
# bajar a celery==3.1.24 o ```celery -A your_app_name worker --pool=solo -l info```
Otra solucion es instalar eventlet `pip install eventlet`
Y utilizar
```s no funciona
$ celery -A your_app_name worker --pool=eventlet
```

# UTILIZAR gevent `pip install gevent`
```s
$ celery -A CeleryTest worker -l debug --pool=gevent
```


