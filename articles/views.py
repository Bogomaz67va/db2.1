from django.shortcuts import render

from articles.models import Article, Scope


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    result = list()
    data = Article.objects.all().order_by(ordering)
    for item in data:
        scope = Scope.objects.filter(article=item).all().order_by('-is_main', 'tag')

        result.append({
            'title': item.title,
            'text': item.text,
            'image': item.image,
            'scopes': scope,
        })
    context = {'object_list': result}

    return render(request, template, context)
