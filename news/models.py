from django.db import models
from django.utils import timezone

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, null=True)
    text = models.TextField()
    image = models.FileField(null=True, blank=True)
    # image = models.ImageField(upload_to=upload_location,
    #         null=True,
    #         blank=True,
    #         width_field="width_field",
    #         height_field="height_field")
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]
