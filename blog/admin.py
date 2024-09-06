from django.contrib import admin
from blog.models import Post, Tag,PostAdmin
# Register your models here.
#admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

# class PostAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#     list_display = ("slug", "published_at")