from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", min_length=3, help_text='Не менее 3х символов',)
    age = forms.IntegerField(label="Возраст клиента",min_value=1, max_value=100,
                             help_text='От 1 до 100')
    required_css_class = "field"
    error_css_class = "error"
    