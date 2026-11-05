from django.db import models

# 作业2：图书馆列表
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="书名")
    author = models.CharField(max_length=100, verbose_name="作者")

    def __str__(self):
        return self.title

# 作业4：留言簿记录
class GuestbookEntry(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名")
    email = models.EmailField(verbose_name="电子邮件")
    content = models.TextField(verbose_name="评价内容")
    is_verified = models.BooleanField(default=False, verbose_name="已验证")

    def __str__(self):
        return self.name
