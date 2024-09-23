from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


# class Publication(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     is_draft = models.BooleanField(default=True)

#     is_blog_post = models.BooleanField(default=False)
#     is_news = models.BooleanField(default=False)
#     is_featured = models.BooleanField(default=False)

#     author = models.ForeignKey("users.User", on_delete=models.CASCADE)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ["-date"]
