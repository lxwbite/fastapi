from tortoise.models import Model
from tortoise import fields


class Publish(Model):
    name = fields.CharField(max_length=32, verbose_name="出版社名称")
    email = fields.CharField(max_length=32, verbose_name="出版社邮箱")


class Author(Model):
    name = fields.CharField(max_length=32, verbose_name="作者")
    age = fields.IntField(verbose_name="年龄")


class Book(Model):
    title = fields.CharField(max_length=32, verbose_name="书籍名称")
    price = fields.IntField(verbose_name="价格")
    # pub_date = models.DateField(verbose_name="出版日期")
    img_url = fields.CharField(max_length=255, null=True, blank=True, verbose_name="")
    bread = fields.IntField(verbose_name="阅读量")
    bcomment = fields.IntField(verbose_name="评论量")
    publishs = fields.ForeignKeyField('models.Publish', related_name='books')
    authors = fields.ManyToManyField('models.Author', related_name='books', description="作者")