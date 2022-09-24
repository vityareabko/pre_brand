from django.shortcuts import render
from django.views.generic.base import View


class MainPage(View):
    def __init__(self):
        pass

    def get(self, request):

        ctx = {}

        return render(request, 'Main/homepage.html', ctx)