from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.CharField(_('description'), max_length=255, null=True, blank=False)
    published_date = models.DateTimeField(_('published date'), default=datetime.now, blank=True)
    author = models.CharField(_('author'), max_length=50)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name=_('post'))
    text = models.TextField(_('text'))
    author = models.CharField(_('author'), max_length=50)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
