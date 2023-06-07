from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %i %i"(
            self.title,
            self.content,
            self.updated_at,
            self.id,
        )
