from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to='plast4ce/projects/')
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('sort_order', '-created_at')

    def __str__(self):
        return self.title


class GalleryImage(TimeStampedModel):
    category = models.CharField(max_length=100, blank=True)
    alt_text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='plast4ce/gallery/')
    is_published = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('sort_order', '-created_at')

    def __str__(self):
        return self.alt_text or f'Gallery image {self.pk}'
