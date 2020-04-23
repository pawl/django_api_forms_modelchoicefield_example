from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import forms


@csrf_exempt
def index(request):
    playlist_form = forms.PlaylistForm.create_from_request(request)
    if not playlist_form.is_valid():
        # Process your validation error
        print(playlist_form.errors)

    # Cleaned valid payload
    payload = playlist_form.cleaned_data
    print(payload)

    return HttpResponse(status=200)
