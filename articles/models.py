from users.models import Account
from django.template.defaultfilters import slugify
from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Kategori Adı")
    description = models.TextField(blank=True, null=True, verbose_name="Kategori Açıklama")
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Kategoriler"


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık", unique=True)
    description = models.CharField(max_length=250, verbose_name="Açıklama", null=True)
    content = models.TextField(verbose_name="İçerik")
    video_link = models.CharField(max_length=250, verbose_name="Youtube Video Adresi", null=True)
    writer = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Yazar",
        blank=True,
        null=True,
    )
    last_edit = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="Düzenleyen Editör",
        null=True,
        blank=True,
        related_name="last_edit_video"
    )
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Tarih")
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name="Kategori"
    )
    image = models.ImageField(upload_to="static/upload/%Y/%m/%portal", default="static/upload/default.jpg",
                              verbose_name="Resim(Önerilen:788x443)")
    slug = models.SlugField(max_length=200, unique=True, null=True, verbose_name="Seo Adres", editable=False)
    views = models.IntegerField(verbose_name="Görüntülenme Sayısı", default=0, editable=False)

    available = models.BooleanField(default=False, verbose_name="Yayına Al")

    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Makaleler"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title.replace('ı', 'i'))
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title