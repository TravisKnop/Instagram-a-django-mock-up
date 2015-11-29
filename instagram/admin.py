from django.contrib import admin

from instagram.models import Name, Gram, Like, Comment, Follower, Following

# Register your models here.
admin.site.register(Name)
admin.site.register(Gram)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Follower)
admin.site.register(Following)
