from django import forms
'''上传表单'''

class UploadForm(forms.Form):
    file = forms.Field(
    widget = forms.ClearableFileInput(attrs={'multiple':True}),
    label = '选择文件...',
    help_text = '最大100M',
    )
