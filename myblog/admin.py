from django.contrib import admin
from .models import article,loginuser
class articleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)

admin.site.register(article,articleAdmin)
admin.site.register(loginuser)





