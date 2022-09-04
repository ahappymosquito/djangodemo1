from django.db import models

# conda activate djangodemo
# python .\manage.py makemigrations
# python .\manage.py migrate


# Create your models here.
class department(models.Model):
    title = models.CharField(verbose_name="标题",max_length=32)

class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="创建时间")

    depart = models.ForeignKey(to ="department",to_field="id",on_delete=models.CASCADE)

    gender_choices = ( (1,"男"), (2,"女") )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)

