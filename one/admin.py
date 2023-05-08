from django.contrib import admin
from one.models import *
# Register your models here.

class MyAdmin(admin.ModelAdmin):
    # list_display = []
    search_fields = ["name"]
    list_filter = ["age"]
    list_per_page = 10
    ordering = ['-id']


class StudentInline(admin.TabularInline):
    model = Student
    extra = 5


class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


admin.site.register(People, MyAdmin)
admin.site.register(IDCard)
admin.site.register(Student)
admin.site.register(Grade, GradeAdmin)
admin.site.register(City)
admin.site.register(Pic)