from django.views import View
from django.shortcuts import render, redirect
from .forms import ArticleForme
from .models import Article
# Create your views here.

class ArticleView(View):
    template_name="public/index.html"
    def get(self,request):
        articles=Article.objects.all()
        form = ArticleForme()
        context={
            'articles':articles,
            'form':form,
        }
        return render(request, self.template_name, context)

    def post(self,request):
        form=ArticleForme(request.POST, request.FILES)

        if form.is_valid():
            title= request.POST.get('title')
            description= request.POST.get('description')
            price = request.POST.get('price')
            image = request.POST.get('image')
            article= Article(
                title=title,
                description=description,
                price=price,
                image=image
            )
            article.save()
            return redirect('article')


