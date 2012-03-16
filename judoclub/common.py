import simplejson as json

def render_json(object):
    from django.http import HttpResponse
    return HttpResponse(json.dumps(object), mime_type='application/jason')


