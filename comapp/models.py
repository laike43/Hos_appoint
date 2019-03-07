from django.db import models

# Create your models here.

class Blog(models.Model):
    column = models.CharField(max_length=300)
    title = models.CharField('标题',max_length=256)
    author = models.ForeignKey('auth.User',blank=True,null=True,on_delete='CASCADE',verbose_name='作者')
    content = models.TextField('内容',default='快乐又一天',blank=True)
    published = models.BooleanField('正式发布',default=True)
    pub_date = models.DateTimeField('发表时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField('更新时间',auto_now=True,null=True)

    def __str__(self):
        return self.title