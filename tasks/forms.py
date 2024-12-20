from django import forms


from . models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_completed']
        


class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'