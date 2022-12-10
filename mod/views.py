from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.core import serializers
from .models import MediaModel
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils.decorators import method_decorator

# Create your views here.
def index(request):
    return render(request, 'mod/index.html', {})

#def room(request, room_name):
#    return render(request, 'mod/room.html', {
#            'room_name': room_name
#            })

@csrf_exempt
#@method_decorator(ensure_csrf_cookie, name='dispatch')
def upload(request):
    if request.method == 'POST':
        media = MediaModel()
        print(request.META)
        media.video = request.FILES['video']
        media.original_file_name = request.FILES['video'].name
        media.filesize = request.META['CONTENT_LENGTH']
        media.save()

        query = MediaModel.objects.get(pk=media.id)
        query = query.__dict__
        del query['_state']
        return JsonResponse(query, safe=False)
       # return redirect('../detail/' + str(media.id))
    else:
        raise Http404('Incorrect Access')

def detail(request, media_id):
    media = MediaModel.objects.get(pk=media_id)
    media = media.__dict__
    del media['_state']
    return JsonResponse(media, safe=False)
   # return HttpResponse(media.video.url)
   # return render(request, 'mod/detail.html', {'media' : media})
