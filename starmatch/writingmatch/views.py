from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import TemplateView
from django.utils import timezone

from .forms import HandleForm

# Create your views here.
class IndexView(TemplateView):
	template_name = 'writingmatch/index.html'


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = HandleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = HandleForm()

    return render(request, 'writingmatch/handle.html', {'form': form})

def thanks(request):
	return HttpResponse("Thank You")
