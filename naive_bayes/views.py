# naive_bayes/views.py
import json

from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from learning_machine.models import Page
from learning_machine.views import PageView
from naive_bayes.manager import Manager


class NaiveBayesView(TemplateView):
    def get(self, request, **kwargs):
        return PageView().get_page(request, 'NaiveBayes')


class GaussianNaiveBayesView(TemplateView):
    def get(self, request, **kwargs):
        gaussianNaiveBayesData = Manager.run_gaussian_naive_bayes()
        return JsonResponse({'gaussianNaiveBayesData': gaussianNaiveBayesData.__dict__})

class GaussianNaiveBayesPlotView(TemplateView):
    def get(self, request, **kwargs):

        imagePath = "./learning_machine/static/images/plot.png"
        from PIL import Image
        Image.init()
        i = Image.open(imagePath)

        response = HttpResponse(content_type='image/png')
        i.save(response, 'PNG')
        return response
