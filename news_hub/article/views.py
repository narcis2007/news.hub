from django.shortcuts import render_to_response, render
from article.models import RawArticle
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import DeleteView,UpdateView # this is the generic view
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.conf import settings




# Create your views here.
def all_articles(request): #all articles who need to be edited
    args={}
    args.update(csrf(request))
    args['articles']=RawArticle.objects.all().filter(toBeEdited=True)[::-1]

    return render(request,'article/articles.html',args)


def published_articles(request):
    args={}
    args.update(csrf(request))
    args['articles']=RawArticle.objects.all().filter(publish=True)[::-1]

    return render(request,'article/published_articles.html',args)

def get_article_by_id(request,article_id=1):
    # form=CommentForm()
    args={}
    args.update(csrf(request))
    # args['form']=form
    args['article']=RawArticle.objects.get(id=article_id)
    # args['comments']=Comment.objects.filter(article=article_id)
    return render(request,'article/article.html',args)

# @login_required
# def get_articles_by_user(request):
#     articles=Article.objects.filter(author=request.user)[::-1]
#     args={}
#     args['articles']=articles
#     return render(request,'article/articles_user.html',args)

# @login_required()
def create_article(request):
    if request.POST:
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save()
            # article.author=request.user
            # article.save()
            messages.success(request,'An article has just been added')
            return HttpResponseRedirect('/articles')

    form=ArticleForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render(request,'article/create_article.html',args)


class delete_article(DeleteView):
    model = RawArticle
    success_url = reverse_lazy('user_articles') # This is where this view will
                                            # redirect the user
    template_name = 'article/delete_article.html'

    def get_success_url(self):
        messages.add_message(self.request,settings.DELETE_MESSAGE,'The article was deleted!')
        return super(delete_article,self).get_success_url()

class update_article(UpdateView):
    model = RawArticle
    fields = ['title','content','suggestions']
    success_url = reverse_lazy('articles') # This is where this view will
                                            # redirect the user
    template_name = 'article/update_entity.html'

    def get_success_url(self):
        messages.success(self.request,'The article was updated!')
        return super(update_article,self).get_success_url()

#
#
# @login_required()
# def add_comment(request,article_id):
#     if request.POST:
#         form=CommentForm(request.POST)
#         if form.is_valid():
#             comment=form.save(commit=False)
#             comment.author=request.user
#             comment.article=Article.objects.get(id=article_id)
#             comment.save()
#             messages.success(request,'A comment has just been added')
#             return HttpResponseRedirect('/articles/get/'+str(article_id))
#     return HttpResponseRedirect('/articles/get/'+str(article_id))
#
# @login_required
# def get_comments_by_user(request):
#     c=Comment.objects.filter(author=request.user)[::-1]
#     args={}
#     args['comments']=c
#     return render(request,'article/comments_user.html',args)
#
# class delete_comment(DeleteView):
#     model = Comment
#     success_url = reverse_lazy('user_comments') # This is where this view will
#                                             # redirect the user
#     template_name = 'article/delete_comment.html'
#
#     def get_success_url(self):
#         messages.add_message(self.request,settings.DELETE_MESSAGE,'The comment was deleted!')
#         return super(delete_comment,self).get_success_url()
#
# class update_comment(UpdateView):
#     model = Comment
#     fields = ['content']
#     success_url = reverse_lazy('user_comments') # This is where this view will
#                                             # redirect the user
#     template_name = 'article/update_entity.html'
#
#     def get_success_url(self):
#         messages.success(self.request,'The comment was updated!')
#         return super(update_comment,self).get_success_url()
#
#
# def like_article(request,article_id):
#     if article_id:
#         article=Article.objects.get(id=article_id)
#         article.likes=article.likes+1
#         article.save()
#     return HttpResponseRedirect('/articles/get/%s' % str(article_id))

'''
de facut: sa caute si in body
'''

# def search_titles(request):
#     search_text=''
#     if request.method=='POST':
#         search_text=request.POST['search_text']
#
#     found_articles=Article.objects.filter(title__icontains=search_text)
#
#
#     return render(request,'article/ajax_search.html',{'found_articles':found_articles})
