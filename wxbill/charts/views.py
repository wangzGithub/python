from django.shortcuts import render
from my_auth.decorators import *


@authenticated_user
def to_index(request):
    return render(request, 'charts/index.html', {})
