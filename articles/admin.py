from django.contrib import admin
from .models import Article, Categories
# Register your models here.



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    prepopulated_fields ={'slug':('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=['writer','last_edit']
    list_display = ('title','writer','last_edit','created_date','available')
    list_filter = ('title','writer','last_edit','created_date','available')

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'writer', None) is None:
            obj.writer = request.user
            obj.save()
        else:
            obj.last_edit = request.user
            obj.save()