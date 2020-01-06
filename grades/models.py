from django.db import models


# Create your models here.
class GradeData(models.Model):
    sid = models.CharField(max_length=20, verbose_name="학번")
    s_name = models.CharField(max_length=20, verbose_name='이름')
    lecture = models.CharField(max_length=20, verbose_name='과목')
    mid_term = models.IntegerField(default=0, verbose_name='중간고사 점수')
    final_term = models.IntegerField(default=0, verbose_name='기말고사 점수')
    year = models.CharField(max_length=20, verbose_name='년도')
    semester = models.CharField(max_length=20, verbose_name='학기')

    def __str__(self):
        return self.s_name+"("+self.lecture+","+self.year+"-"+self.semester+")"

