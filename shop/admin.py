from django.contrib import admin
from .models import Course, Category

admin.site.site_title = "My courses"
admin.site.site_header = "Course Admin"
admin.site.index_title = "Courses admin area"


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'id')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'id')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    inlines = [CoursesInline]


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
