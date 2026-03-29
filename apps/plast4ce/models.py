"""
Future CMS models (not migrated yet — design only).
Wire views and admin when you are ready to persist content.
"""

from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Service(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    body = models.TextField(blank=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='plast4ce/projects/', blank=True)

    class Meta:
        abstract = True


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=120, blank=True)
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)

    class Meta:
        abstract = True


class TeamMember(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    role = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='plast4ce/team/', blank=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    sku = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        abstract = True
