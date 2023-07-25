from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    html_content = models.TextField(blank=True)
    css_content = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)

    def publish(self):
        self.save()

    class Meta:
        verbose_name = 'page'
        verbose_name_plural = 'pages'


