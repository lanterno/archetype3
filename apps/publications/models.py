from django.contrib.postgres.fields import ArrayField
from django.db import models
from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


class Event(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Publication(models.Model):
    class Status(models.TextChoices):
        DRAFT = "Draft"
        PUBLISHED = "Published"

    title = models.CharField(max_length=350)
    slug = models.SlugField(max_length=150, unique=True)
    content = HTMLField()
    preview = HTMLField()

    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
        help_text="With Draft chosen, will only be shown for admin users on the site.",
    )
    keywords = TaggableManager(verbose_name="Keywords", blank=True)
    is_blog_post = models.BooleanField(default=False)
    is_news = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    published_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    post = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()

    author_name = models.CharField(max_length=150)
    author_email = models.EmailField()
    author_website = models.URLField(blank=True, null=True)

    is_approved = models.BooleanField(default=False, help_text="Show on website?")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author_name} -> {self.post.title}"

    class Meta:
        ordering = ["-created_at"]
