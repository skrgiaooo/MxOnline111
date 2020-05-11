import xadmin
from apps.courses.models import Course,Lesson,Video,CourseResource

class CourseAdmin(object):
    #显示字段
    list_display = ['id','name','desc','teacher_tell']
    #搜索字段
    search_fields = ['id','name','desc','teacher_tell']
    #筛选
    list_filter = ['id','name','desc','teacher_tell']
    pass
class LessonAdmin(object):
    pass
class VideoAdmin(object):
    pass
class CourseResourceAdmin(object):
    pass

xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)

