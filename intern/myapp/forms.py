from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    UserCreationForm,PasswordChangeForm,AuthenticationForm
    )
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import (
    FileExtensionValidator
)

from .models import User,UserImage

class SignUpForm(UserCreationForm):
    img = forms.ImageField(
        required=False, validators=[FileExtensionValidator(["jpg", "jpeg", "png"])],
    )
    class Meta:
        model = User
        """
        Django標準のUserに存在するfieldです。
        上のimgは元々のものには無いので、自分で作ります。
        """
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    #27-32行目は型となっているからこのまま覚える        
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                _("This account is inactive."),
                code='inactive',
            )

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'

class MailSettingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
           default_label = str(field.label)
           new_label = "new" + default_label
           field.label = new_label

class UserNameSettingForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',)
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       for field in self.fields.values():
           default_label = str(field.label)
           new_label = "new" + default_label
           field.label = new_label

class ImageSettingForm(forms.ModelForm):
    class Meta:
        model = UserImage
        exclude = ("user",)

class PasswordChangeForm(PasswordChangeForm):
    """
    Django標準パスワード変更フォーム
    Djangoはユーザモデルに未加工の (単なるテキストの) パスワードは保存せず
    ハッシュ値でのみ保存します。
    したがって、ユーザのパスワード属性を直接操作できない。
    よってパスワード編集のために標準で用意されているformを使います。
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# 友達の中から任意のユーザーを検索
class FriendsSearchForm(forms.Form):
    keyword = forms.CharField(label='検索',required=False,widget=forms.TextInput(attrs={'placeholder': 'ユーザー名で検索'}))
    
# トークの送信のためのform
# メッセージを送信するだけで、誰から誰か、時間は全て自動で対応できるのでこれだけで十分
class TalkForm(forms.Form):
    talk = forms.CharField(label='talk')

class TweetForm(forms.Form):
    tweet = forms.CharField(label='tweet')
