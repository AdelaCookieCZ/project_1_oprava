from django.http import HttpResponse
from django.template.response import TemplateResponse


def homepage(request):
    return TemplateResponse(request, 'homepage.html')

