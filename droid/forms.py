from django import forms
from .models import APK
#class DocumentForm(forms.Form):
 #   docfile = forms.FileField(
  #      label='Select a file',
   #     help_text='max. 42 megabytes'
    #)

class APKForm(forms.Form):
    apk = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
    
    class Meta:
        model = APK
