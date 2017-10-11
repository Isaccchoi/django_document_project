from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    debut_date = models.DateField()
    # through_fields안에 적는 순서는 (Source, Target)
    members = models.ManyToManyField(Idol, through='Membership', through_fields=('group', 'idol',), )

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(Idol, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # recommender = models.ForeignKey(
    #     Idol,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     # 연결되어 있는 ForeignKey가 2개로 역참조시 필드 이름에서 충돌이 날 수 있음
    #     # 그 역참조시 이름 충돌을 피하기 위해 한 필드에 related_name을 따로 지정
    #     related_name='recommend_membership_set',
    # )
    recommenders = models.ManyToManyField(
        Idol,
        null=True,
        # ManyToMany또한 ForeignKey로 접근이 가능하기 때문에
        # ManyToMany에도 역참조 오류는 동일 하게 발생, related_name을 지정하여 ForeignKey때와 동일 하게 해결
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name} ' \
               f'{self.idol.name} ' \
               f'{self.is_active}'
