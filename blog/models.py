import markdown
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags


class Category(models.Model):
    """定义模型类
    分类
    """
    name = models.CharField('分类名',max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    定义模型类
    标签名
    """
    name = models.CharField('标签名',max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    模型类
    文章
    """
    # 文章标题
    title = models.CharField('标题', max_length=70)

    # 文章正文
    body = models.TextField('正文')

    # 文章创建时间
    created_time = models.DateTimeField('创建的时间', default=timezone.now)

    # 文章修改时间
    modified_time = models.DateTimeField('修改的时间')

    # 文章摘要
    excerpt = models.CharField('摘要', max_length=200, blank=True)

    # 文章外键（一对多）：分类名
    # 一篇文章只能对应一个分类名，一个分类中有多篇文章
    category = models.ForeignKey(Category,verbose_name='分类', on_delete=models.CASCADE)

    # 文章外键（多对多）：标签名
    # 一篇文章可以有多个标签，一个标签可以有多篇文章
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)

    # 文章外键（一对多）：作者
    # 一篇文章有只能有一个作者，一个作者可以有多篇文章
    author = models.ForeignKey(User,verbose_name='作者', on_delete=models.CASCADE)

    # 阅读量
    views = models.PositiveIntegerField(default=0, editable=False)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    # 定义函数__str__
    def __str__(self):
        return self.title

    # 定义函数save（）
    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        # 首先实例化一个 Markdown 类，用于渲染 body 的文本。
        # 由于摘要并不需要生成文章目录，所以去掉了目录拓展。
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        # 第一：先将 Markdown 文本渲染成 HTML 文本
        # 第二：strip_tags 去掉 HTML 文本的全部 HTML 标签
        # 第三：从文本摘取前 54 个字符赋给 excerpt
        self.excerpt = strip_tags(md.convert(self.body))[:0]
        super().save(*args, **kwargs)

    # 定义get_absolute_url()
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    # 定义函数increase_views（）
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])














