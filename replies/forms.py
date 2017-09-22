from django.forms import ModelForm
from django import forms
from replies.models import Reply

class ReplyForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'id': 'reply','class':'form-control','placeholder':'reply'}))
    class Meta:
        model = Reply
        fields = ['text']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].label = 'Reply'
