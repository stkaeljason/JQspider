# from django.shortcuts import render
# from kombu import Connection, Exchange, Queue,Consumer
# from kombu.async import Hub
from . import tasks


from django.shortcuts import HttpResponse


def add_task(request):
    tasks.add.delay(3,4)
    return HttpResponse('success add the add_task')

