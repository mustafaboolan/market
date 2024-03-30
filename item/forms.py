from django import forms
from .models import Item

STYLE_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','description','price','image',]
     
        # html_tags this use to add style to html elements
        widgets = {
            'category':forms.Select(attrs={'class':STYLE_CLASSES}),
            'name':forms.TextInput(attrs={'class':STYLE_CLASSES}),
            'description':forms.Textarea(attrs={'class':STYLE_CLASSES}),
            'price':forms.TextInput(attrs={'class':STYLE_CLASSES,'type':'number'}),
            'image':forms.FileInput(attrs={'class':STYLE_CLASSES}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','description','price','image','is_sold']
     
        # html_tags this use to add style to html elements
        widgets = {          
            'name':forms.TextInput(attrs={'class':STYLE_CLASSES}),
            'description':forms.Textarea(attrs={'class':STYLE_CLASSES}),
            'price':forms.TextInput(attrs={'class':STYLE_CLASSES,'type':'number'}),
            'image':forms.FileInput(attrs={'class':STYLE_CLASSES}),
        }





