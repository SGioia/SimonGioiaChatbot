from django import forms


class ContactForm(forms.Form):
    Question = forms.CharField(required=True, label='QUESTION PLACEHOLDER - FOR WEBPAGE EMBEDDED CHATBOT')

