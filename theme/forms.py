from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,
                              required=True,
                              widget=forms.TextInput(attrs={'placeholder':
                                                            'Subject'}))
    message = forms.CharField(max_length=5000,
                              required=True,
                              widget=forms.Textarea(attrs={'placeholder':
                                                           'Hello,'}))
    name = forms.CharField(max_length=100, required=True,
                           widget=forms.TextInput(attrs={'placeholder':
                                                         'Name'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':
                                                            'E-mail'}),
                              required=True)
