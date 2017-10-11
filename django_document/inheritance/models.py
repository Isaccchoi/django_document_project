from django.db import models


class School(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    # abstractBaseClass에서 상송진행시 ForeignKey의 related_name을 지정하면 오류 발생 - 역참조 이름이 같게됨
    # 그렇기때문에 같지 않게 하기 위해 $(app_label)s 및 %(class)s를 사용해 충돌 제거
    school = models.ForeignKey(School, blank=True, null=True, related_name='%(app_label)s_%(class)s_set')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Teacher(CommonInfo):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.name
