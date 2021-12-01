from django import forms

class EditForm(forms.Form):
    title = forms.CharField(label= '', widget= forms.TextInput
        (attrs={'placeholder':'Title', 'style': 'width: 1000px ; height: 70px ; font-size: xx-large'}), max_length=65)
    content = forms.CharField(label='', widget= forms.Textarea
        (attrs={'placeholder':'Content', 'style': 'width: 1000px ; height: 500px ; text-align: left'}))