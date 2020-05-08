import xadmin
from apps.courses.models import Course

class CourseAdmin(object):
    #显示字段
    list_display = ['id','name','desc','teacher_tell']
    #搜索字段
    search_fields = ['id','name','desc','teacher_tell']
    #筛选
    list_filter = ['id','name','desc','teacher_tell']
    pass

xadmin.site.register(Course,CourseAdmin)
