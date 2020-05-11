from django.db import models
from apps.users.models import BaseModel
from apps.users.models import UserProfile


# Create your models here.
class City(BaseModel):
    city_name = models.CharField(max_length=10, verbose_name="城市名")

    class Meta:
        verbose_name = '机构所属城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.city_name


class CourseOrg(BaseModel):
    orgname = models.CharField(max_length=20, verbose_name="机构名称", default='')
    orglable = models.CharField(max_length=200, verbose_name="机构标签", default='')
    orgtype = models.CharField(max_length=20, verbose_name="机构类别", choices=(('jg', "培训机构"), ("gr", "个人"), ("gx", "高校")),
                               default='')
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    read_nums = models.IntegerField(verbose_name='收藏数', default=0)
    orgaddress = models.CharField(max_length=100, verbose_name="机构地址", default='')
    people_nums = models.IntegerField(verbose_name="学习人数", default=0)
    class_nums = models.IntegerField(verbose_name="课程数", default=0)
    orgauth = models.BooleanField(verbose_name="是否认证", default=False)
    orggold = models.BooleanField(verbose_name="是否金牌", default=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市", default='')
    orgimage = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)

    class Meta:
        verbose_name = '教育机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.orgname


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    teaname = models.CharField(max_length=20, verbose_name="教师名", default='')
    workyear = models.IntegerField(verbose_name="工作年限(年)", default=0)
    company = models.CharField(max_length=20, verbose_name="就职公司", default='')
    position = models.CharField(max_length=20, verbose_name="公司职位", default='教师')
    Characteristic = models.CharField(max_length=200, verbose_name="特点", default='')
    company = models.CharField(max_length=20, verbose_name="就职公司", default='')
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    collection_nums = models.IntegerField(verbose_name="收藏数", default=0)
    age = models.IntegerField(verbose_name='年龄', default=0)
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teaname
