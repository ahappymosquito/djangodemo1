from django.db import models

# conda activate djangodemo
# python .\manage.py makemigrations
# python .\manage.py migrate


# Create your models here.
class department(models.Model):
    title = models.CharField(verbose_name="标题",max_length=32)

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    name = models.CharField(verbose_name="姓名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额",max_digits=10,decimal_places=2,default=0)
    create_time = models.DateTimeField(verbose_name="创建时间")

    depart = models.ForeignKey( verbose_name="部门",to ="department",to_field="id",on_delete=models.CASCADE)

    gender_choices = ( (1,"男"), (2,"女") )
    gender = models.SmallIntegerField(verbose_name="性别",choices=gender_choices)



class prettynum(models.Model):
    phonenumber = models.CharField(verbose_name='电话号码',max_length=11)

    price = models.IntegerField(verbose_name='价格',default=10)

    level_choices = (
        (1,"1极"),
        (2, "2极"),
        (3, "3极"),
        (4, "4极"),
    )

    level = models.SmallIntegerField(verbose_name="级别",choices=level_choices,default=1)

    status_choices = (
        (1,"已使用"),
        (0,"未使用")
    )

    status = models.SmallIntegerField(verbose_name="状态",choices=status_choices,default=0)


