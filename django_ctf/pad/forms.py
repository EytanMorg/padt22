from django import forms

class flagCheck(forms.Form):
    flag = forms.CharField(label='Flag:', widget=forms.TextInput(attrs={'placeholder': "pad_t22/...\\", 'class': "form-control"}))
