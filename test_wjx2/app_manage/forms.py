#导入表单模块
from django import forms
#导入from表单模块
from django.forms import widgets
from app_manage.models import Module
from app_manage.models import Project


class ProjectForm(forms.Form):
    #表单标题的名称
    name = forms.CharField(label='名称',
                           max_length=100,
                           widget=widgets.TextInput(attrs={'class': "form-control"}))
    describe = forms.CharField(label="描述",
                               widget=widgets.Textarea(attrs={'class': "form-control"}))
    #true和false就是代表必填非必填
    status = forms.BooleanField(label="状态", required=False,
                                widget=widgets.CheckboxInput()
                                )

#这两个功能是一样的
class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name","describe","status"]



#模块的表单,ModelForm属于一个表单
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ["project","name","describe"]



