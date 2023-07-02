from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    publication_url = models.URLField()
    image = models.FilePathField(path='/img')

    def __str(self):
        return self.title
