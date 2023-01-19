from django import forms
from Models.models import Variable


# formulario para Variable
class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = ['description','name', 'scale']
        labels={
            'description':'Descripción',
            'name':'Nombre'
        } 
        widgets={
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean_description(self):
        description=self.cleaned_data['description']
        for c in description:
            if c in'`!@#$%^&*()_=+-}{][></"\|01234567879~':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return description 
    def clean_name(self):
        name=self.cleaned_data['name']
        for c in name:
            if c in'`!@#$%^&*()_=+-}{][></"\|0123456789~\n':
              raise forms.ValidationError('Solo se aceptan letras en este campo.') 
        return name 