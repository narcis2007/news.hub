__author__ = 'narcis'
from django.conf.urls import include, url
from . import views
urlpatterns=[
    url(r'^$',views.all_articles ,name='articles'),
    url(r'^published/$',views.published_articles ,name='published_articles'),
    url(r'^get/(?P<article_id>\d+)/$',views.get_article_by_id),
    url(r'^create/$',views.create_article),
    # url(r'^like/(?P<article_id>\d+)/$',views.like_article),
    # url(r'search/$',views.search_titles),
    # url(r'add_comment/(?P<article_id>\d+)/$',views.add_comment),
    # url(r'^get/user/$',views.get_articles_by_user,name='user_articles'),
    url(r'^delete/(?P<pk>\d+)/$',views.delete_article.as_view(), name='delete_article'),
    url(r'^update/(?P<pk>\d+)/$',views.update_article.as_view(), name='update_article'),
    # url(r'^get/user/comments/$',views.get_comments_by_user,name='user_comments'),
    # url(r'^delete/comment/(?P<pk>\d+)/$',views.delete_comment.as_view(), name='delete_comment'),
    # url(r'^update/comment/(?P<pk>\d+)/$',views.update_comment.as_view(), name='update_comment'),
]