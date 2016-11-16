from __future__ import unicode_literals

import json

from django.http import HttpResponse


MENSAJES_ERROR = [
    u'Permiso denegado.',
    u'No tiene permiso para modificar la inscripcion.',
    u'No tiene permiso para realizar esta accion.'
]


def bad_json(mensaje=None, error=None, extradata=None):
    data = {'result': 'bad'}
    if mensaje:
        data.update({'mensaje': mensaje})
    if error:
        if error == 0:
            data.update({"mensaje": "Incorrect request"})
        elif error == 1:
            data.update({"mensaje": "Error saving data"})
        elif error == 2:
            data.update({"mensaje": "Error deleting data"})
        elif error == 3:
            data.update({"mensaje": "Error getting data"})
        elif error == 4:
            data.update({"mensaje": "You dont have permission to perform this action"})
        elif error == 5:
            data.update({"mensaje": "Error generating the information"})
        else:
            data.update({"mensaje": "System error"})
    if extradata:
        data.update(extradata)
    return HttpResponse(json.dumps(data), content_type="application/json")


def ok_json(data=None):
    if data:
        if 'result' not in data.keys():
            data.update({"result": "ok"})
    else:
        data = {"result": "ok"}
    return HttpResponse(json.dumps(data), content_type="application/json")
