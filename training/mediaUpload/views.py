from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import os
from django.conf import settings
import datetime
from .models import Files

def index(request):
    return render(request, 'index.html')

def upload_img(request):
    if request.method == 'POST':
        """
            handles: <InMemoryUploadFile> grava em memoria.
            handles: <TemporaryUploadFile> grava no hd/ssd.
        """
        file = request.FILES.get('file')

        """ file.name | file.size | file.file |file.chunks """

        img = Image.open(file)
        path_save_img = os.path.join(settings.BASE_DIR, f'media/{file.name}-{datetime.datetime.now()}.{img.format}')
        img.save(path_save_img)

        Files(title="file_name", file=file).save()

        return HttpResponse("FILES UPLOAD")
    else:
        return HttpResponse("N.D")