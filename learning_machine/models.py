from django.db import models


class Page(models.Model):

    id = models.CharField(primary_key=True, max_length=30, null=False)
    title = models.CharField(max_length=30, null=False)
    body = models.CharField(max_length=30, null=False)


class NavigationItem(models.Model):

    name = models.CharField(primary_key=True, max_length=30, null=False)
    url = models.URLField(primary_key=True, null=False)


