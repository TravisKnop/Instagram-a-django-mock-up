from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import datetime

__author__ = 'travisknop'


class IndexView(View):

    def index(self):
        return HttpResponse("Instagramz!")

    def get(self, request):
        return HttpResponse("This is stupid!")

    def post(self, request):
        return HttpResponse("This is a stupid post request!")
