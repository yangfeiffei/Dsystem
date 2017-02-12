from django import forms
from django.forms import ModelForm
from daily import models



class DailyModelForm(ModelForm):
    class Meta:
        model = models.Daily
        fields = ['content','categories','hours']

    def __new__(cls, *args, **kwargs):

        for field_name in cls.base_fields:
            field = cls.base_fields[field_name]
            field.widget.attrs.update({"class": "form-control"})

        return forms.ModelForm.__new__(cls)

# from django.db import models
# from django.contrib.auth.models import User
#
# # Create your models here.
#
# class UserProfile(models.Model):
#     '''
#     用户相关
#     '''
#     user = models.OneToOneField(User)
#     name = models.CharField(u'姓名', max_length=16, )
#     signature = models.CharField(u'个性签名', max_length=255,
#                                  blank=True, null=True)
#     head_portrait = models.ImageField(u"用户头像",
#                                  upload_to="uploads/userprofile",
#                                  default="uploads/userprofile/default_user_head.ipg")
#
#     def __str__(self):
#         return self.user.username
#
#
# class Categories(models.Model):
#     '''
#     分类相关
#     '''
#
#     name = models.CharField(u'分类名', max_length=16)
#     difficulty_choices = (
#         (3, '高'),
#         (2, '中'),
#         (1, '低'),
#     )
#     difficulty = models.IntegerField(u'难度', choices=difficulty_choices, default=2)
#     important_degree = models.IntegerField(u'重要程度', choices=difficulty_choices, default=2)
#     memo = models.CharField(u'备注', max_length= 128)
#
#     def __str__(self):
#         return self.name
#
#
#
# class Daily(models.Model):
#     '''
#     日报相关
#     '''
#     upload_date = models.DateField(u'日期')
#     user = models.ForeignKey(UserProfile, verbose_name=u'所属用户')
#     content = models.TextField(u'日报内容')
#     categories = models.ManyToManyField(Categories,
#                                         verbose_name=u'日报分类',
#                                         related_name='my_categories',
#                                         )
#     status_chioces = (
#         (0,u'编写'),
#         (1,u'审核'),
#         (2,u'锁定'),
#     )
#     status = models.IntegerField(u'日报状态',
#                                  choices=status_chioces,
#                                  default=0,
#                                  )
#     hours = models.FloatField(u'工作时间', default=7.5)
#     comment = models.TextField(u'评语', null=True, blank=True)
#
#
#     def __str__(self):
#         return '%s,%s日报' %(self.user.name, self.upload_date)