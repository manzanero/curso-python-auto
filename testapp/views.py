from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def get_example(request):
    response = {
        'request': {
            'time': datetime.now().isoformat(),
            'method': request.method,
            'path': request.path,
            'params': request.GET,
            'headers': dict(request.headers),
        }
    }

    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})


@csrf_exempt
def post_example(request):
    response = {
        'request': {
            'time': datetime.now().isoformat(),
            'method': request.method,
            'path': request.path,
            'params': request.GET,
            'headers': dict(request.headers),
            'body': request.body.decode(),
        }
    }

    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})
