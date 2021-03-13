from django.shortcuts import render


def to_index(request):
    return render(request, 'my_auth/index.html', {})


def to_test(request):
    return render(request, 'my_auth/test.html', {})
