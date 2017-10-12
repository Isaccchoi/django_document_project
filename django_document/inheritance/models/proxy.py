from django.db import models

__all__ = (
    'Champion',
)


class Champion(models.Model):
    CHOICE_TYPE = (
        ('magician', '마법사'),
        ('supporter', '서포터'),
        ('ad', '원거리 딜러'),
    )
    champion_type = models.CharField(max_length=20, choices=CHOICE_TYPE)
    rank = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} - ({self.champion_type})'


# 가상으로 만든 Supporter 모델에 대해 매니저를 커스터마이징 할 수 있음
class SupporterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(champion_type='supporter')


class Supporter(Champion):
    objects = SupporterManager()

    class Meta:
        proxy = True

    def buy_supporter_item(self):
        print(f'{self.name}은 서포터 아이템을 샀다')
