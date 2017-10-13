# naive_bayes/urls.py
from django.conf.urls import url
from naive_bayes import views

urlpatterns = [
    url(r'^naiveBayes/$', views.NaiveBayesView.as_view()),
    url(r'^naiveBayes/gaussian/$', views.GaussianNaiveBayesView.as_view()),
    url(r'^naiveBayes/gaussian/plot$', views.GaussianNaiveBayesPlotView.as_view()),
]
