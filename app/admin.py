from django.contrib import admin
from django.utils.safestring import mark_safe
from app.models import Teacher, ClassInfo, Timetable, CommonInfo, Gallery

class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'display_order'
    ]

class ClassInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'introduce',
        'get_color'
    ]

    def get_color(self, obj):
        return mark_safe('<div style="color:%s;">%s</div>' % (obj.color, obj.color))
    get_color.short_description = u"컬러코드"

class TimetableAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'classinfo',
        'day_of_week',
        'class_room',
        'start_time',
        'end_time'
    ]
    list_filter = [
        'classinfo',
        'day_of_week',
        'class_room'
    ]

    def get_queryset(self, request):
        queryset = super(TimetableAdmin, self).get_queryset(request)
        queryset = queryset.select_related('classinfo')
        return queryset

    def get_classname(self, obj):
        return obj.classinfo.name

class CommonInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'community_text',
        'naver_text',
        'instagram_text',
        'facebook_text',
        'timetable_text'
    ]

class GalleryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'get_photo',
        'display_order'
    ]

    def get_photo(self, obj):
        return mark_safe('<img src="%s" width="100px" />' % (obj.photo.url))
    get_photo.short_description = u"사진"

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(ClassInfo, ClassInfoAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(CommonInfo, CommonInfoAdmin)
admin.site.register(Gallery, GalleryAdmin)
