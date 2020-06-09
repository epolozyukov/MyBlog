from django.contrib import admin

from blog.models import Post, Category
from projects.models import Project

#for this project the default configuration is enough that is why i do not implement classes
class PostAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)