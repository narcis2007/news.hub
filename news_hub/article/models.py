from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# Create your models here.


def get_upload_file_name(instance,filename):
        return 'uploaded_files/' + str(datetime.now())+'_' + filename

class RawArticle(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    # thumbnail=models.FileField(upload_to=get_upload_file_name,null=True,blank=True)
    email=models.EmailField()
    toBeEdited=models.BooleanField(default=True)
    publish=models.BooleanField(default=False)
    suggestions=models.TextField();

    def save(self, *args, **kwargs):
        # if self.toBeEdited== True:
        #     self.toBeEdited=False
        '''if it was edited set toBeEdited to false '''
        super(RawArticle, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

# @receiver(pre_delete, sender=Article)
# def article_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     if instance.thumbnail:
#         instance.thumbnail.delete(False)
#
# class Comment(models.Model):
#     content=models.TextField()
#     author=models.ForeignKey(User)
#     article=models.ForeignKey(Article)
#
#     def __unicode__(self):
#         return str(self.id)+'_'+self.content