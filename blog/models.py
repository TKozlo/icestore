from audioop import reverse
from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'PostCategory'
        verbose_name_plural = 'PostCategoties'



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']
        verbose_name = 'PostTag'
        verbose_name_plural = 'PostTags'





class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= 'Published')
    photo = models.ImageField(upload_to = 'post_image/%Y-%m-%d', blank = True)
    views = models.IntegerField(default = 0, verbose_name='Numbers of views')
    category = models.ForeignKey(Category, on_delete= models.PROTECT, related_name= 'posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})  # {{ post.get_absolute_url }}

    class Meta:
        ordering = ['-created_at']