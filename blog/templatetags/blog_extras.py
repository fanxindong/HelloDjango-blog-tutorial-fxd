from django import template
from ..models import Post, Category, Tag

register = template.Library()

# 定义“最新文章”模板标签
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_post(context, num = 5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }

# 定义“归档”模板标签
@register.inclusion_tag('blog/inclusions/_archieves.html', takes_context=True)
def show_archieves(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC')
    }

# 定义“分类”模板标签
@register.inclusion_tag('blog/inclusions/_categories.html',takes_context=True)
def show_categories(context):
    return {
        'categories_list': Category.objects.all()
    }

# 定义“标签云”模板标签
@register.inclusion_tag('blog/inclusions/_tages.html', takes_context=True)
def show_tages(context):
    return {
        'tag_list': Tag.objects.all()
    }



