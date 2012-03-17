import simplejson as json

def render_json(object):
    from django.http import HttpResponse
    return HttpResponse(json.dumps(object), mimetype='application/json')


