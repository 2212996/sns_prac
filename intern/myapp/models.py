from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.utils.translation import gettext_lazy as _
import datetime

class User(AbstractUser):
    pass

class UserImage(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_img")
    image = models.ImageField(verbose_name="画像",upload_to="images")
    def __str__(self):
        return "{}の写真".format(self.user)

# トーク内容を全てdatbaseに保存する形をとる
# ＞１個のトーク内容に紐づける情報は
# ＞〇誰が送ったのか
# ＞〇誰に送ったのか
# ＞〇いつ送ったのか
# という情報
class Talk(models.Model):
    # メッセージ
    talk = models.CharField(max_length = 500)
    # 誰から
    talk_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="talk_from")
    # 誰に
    talk_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="talk_to")
    # 時間は
    time = models.DateTimeField(null=True)
    def __int__(self):
        return "{}>>{}".format(self.talk_from, self.talk_to)

class Tweet(models.Model):
    # メッセージ
    tweet = models.CharField(max_length = 500)
    # 誰から
    tweet_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweet_from")
    # 時間は
    time = models.DateTimeField(null=True)