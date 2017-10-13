# naive_bayes/views.py
from string import Template

from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView

from learning_machine.manager import Manager
from learning_machine.models import Page


class PageView(TemplateView):

    template_name = 'learning_machine/page.html'
    model = Page

    def get_page(self, request, page_name):

        try:
            page = Manager.get_page(page_name)
        except self.model.DoesNotExist:
            raise Http404(Template('Page ${pageName} does not exist').substitute(locals()))
        return render(request, self.template_name, context={'page': page})
