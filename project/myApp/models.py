from django.db import models

# Create your models here.

#自定义模型管理器
class studentManger(models.Manager):

    def get_queryset(self):

        return super(studentManger,self).get_queryset().filter(isDelete=False)



#关联班级表
class Grades(models.Model):

    gname     = models.CharField(max_length=20)
    gdate     = models.DateTimeField()
    ggirlnum  = models.IntegerField()
    gboynum   = models.IntegerField()
    isDelete  = models.BooleanField(default=False)

    def __str__(self):
        return self.gname
    # class Meta():
    #     db_table = "grades"
    #     #按id对默认字段进行升序排序，['-d']为倒序
    #     ordering = ['id']

#关联学生表
class Students(models.Model):
    # 对默认的管理器重新命名
    # stu = models.Manager()
    #
    # # 使用自定义的管理器
    # stuManager = studentManger()

    sname    = models.CharField(max_length=20)
    sgender  = models.BooleanField(default=True)
    sage     = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #设置外键
    sgrade   = models.ForeignKey("Grades")

    def __str__(self):
        return self.sname
    # class Meta():
    #     db_table = "students"
    #     #按id对默认字段进行升序排序，['-d']为倒序
    #     ordering = ['id']stu

    @classmethod
    def creatStudent(cls,sname,sgender,sage,scontent,sgrade,isDelete=False):

        stu = cls(sname=sname,sgender=sgender,sage=sage,scontend=scontent,sgrade=sgrade,isDelete=isDelete)

        return stu