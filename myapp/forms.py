from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label="Value 1",required=False,widget=forms.TextInput(attrs={'class':'form.control'}))
    num2=forms.CharField(label="Value 2",required=False,widget=forms.TextInput(attrs={'class':'form.control'}))
    # Email=forms.EmailField(required=False,widget=forms.TextInput(attrs={'class':'form.control'}))





