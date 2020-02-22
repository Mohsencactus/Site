from django import forms
from django.contrib.auth import authenticate,get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label= "نام کاربری")
    password = forms.CharField(widget=forms.PasswordInput , label= "رمز عبور")
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('این نام کاربری وجود ندارد')
            if not user.check_password(password):
                raise forms.ValidationError('رمز وارد شده اشتباه است')
            if not user.is_active:
                raise forms.ValidationError('این حساب مسدود شده است')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='ایمیل')
    username = forms.CharField(label= "نام کاربری")
    first_name = forms.CharField(label= "نام")
    last_name = forms.CharField(label= "نام خانوادگی")
    password = forms.CharField(widget=forms.PasswordInput , label= "رمز عبور")
    password2 = forms.CharField(widget=forms.PasswordInput , label= "تکرار رمز عبور")

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        cleaned_data = super(UserRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password2")
        if password != confirm_password:
            raise forms.ValidationError("رمز های وارد شده یکسان نیست")
        if email_qs.exists():
            raise forms.ValidationError("این ایمیل قبلا ثبت شده است")
        return super(UserRegisterForm, self).clean(*args, **kwargs)