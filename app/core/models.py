from django.db import models

class ModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True).order_by('id')
    
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = ModelManager()
    all_objects = models.Manager()

    def delete(self):
        if not self.active:
            raise(__class__.__name__ + " is already deleted.")

        self.active = False

    class Meta:
        abstract = True