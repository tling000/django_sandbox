from django.db import models

# Create your models here.
class Memo(models.Model):
    """
    メモ
    """

    title = models.CharField(max_length=100, verbose_name='タイトル', default='')
    content = models.TextField(verbose_name='内容', default='')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
