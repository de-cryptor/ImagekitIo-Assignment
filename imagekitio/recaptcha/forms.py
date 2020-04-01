from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Username"
            }
        ) )
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                "class" : "form-control",
                "placeholder" : "Email"
            }
        )
    )
    password1 = forms.CharField(label="Password",
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                "placeholder":"Password"
            }
        )
    )

    password2 = forms.CharField(label="Confirm Password",
        widget = forms.PasswordInput(
            attrs={
                "class":"form-control",
                "label":"Confirm Password",
                "placeholder":"Re-enter Password"
            }
        )
    )

    def clean(self):
        data = self.cleaned_data
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if(password1 != password2):
            raise forms.ValidationError("Password Should Match")
        return data
