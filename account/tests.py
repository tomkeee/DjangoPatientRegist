from django.test import TestCase

# Create your tests here.
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    def clean_username(self):
        username=self.cleaned_data.get("username")
        qs= User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("This user does not exist.")
        return username

    def clean_password(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")

        user_qs=User.objects.filter(username__iexact=username)
        if user_qs.exists():
            user_a=user_qs.first()
            if not user_a.check_password(password):
                raise forms.ValidationError("Given password is not correct")
        return password