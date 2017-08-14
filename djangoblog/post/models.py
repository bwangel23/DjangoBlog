from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse

from djangoblog.user.models import User


# Create your models here.
@python_2_unicode_compatible
class Tag(models.Model):
    """
    文章标签
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    abstract = models.CharField(max_length=300, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return "%d: %s" % (self.id, self.title)

    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
