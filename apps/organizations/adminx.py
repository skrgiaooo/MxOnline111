import xadmin
from apps.organizations.models import City,CourseOrg,Teacher
class CityAdmin(object):
    #显示字段
    # list_display = ['id','name','desc','teacher_tell']
    # #搜索字段
    # search_fields = ['id','name','desc','teacher_tell']
    # #筛选
    # list_filter = ['id','name','desc','teacher_tell']
    pass
class CourseOrgAdmin(object):
    pass
class TeacherAdmin(object):
    pass
xadmin.site.register(City,CityAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
