from django import forms

from .models import ConversationMessage

class ConversationMessageForm(forms.ModelForm):
    