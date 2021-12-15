from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='Product Title', widget = forms.TextInput(attrs = {'placeholder' : 'Your Title'}))
    email       = forms.EmailField()
    description = forms.CharField(
        required = False, 
        widget = forms.Textarea(attrs={
            'placeholder' : 'Product Description',
            'class'       : 'new-class-name two',
            'id'          : 'my_id_for_textarea',
            'rows'        : 20,
            'cols'        : 35
        }))
    price       = forms.DecimalField(initial=1.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs): #making sure the title has some specific charcs
        title = self.cleaned_data.get('title')

        if not 'CFE' in title:
            raise(forms.ValidationError("This is not a valid title"))
        else:
            return(title)

    def clean_email(self, *args, **kwargs): #making sure the title has some specific charcs
        email = self.cleaned_data.get('email')

        if not email.endswith('edu'):
            raise(forms.ValidationError("This is not a valid email"))
        else:
            return(email)
            

class RawProductForm(forms.Form):
    title       = forms.CharField(label='Product Title', widget = forms.TextInput(attrs = {'placeholder' : 'Your Title'}))
    description = forms.CharField(
        required=False, 
        widget = forms.Textarea(attrs={
            'placeholder' : 'Product Description',
            'class'       : 'new-class-name two',
            'id'          : 'my_id_for_textarea',
            'rows'        : 20,
            'cols'        : 35
        }))
    price       = forms.DecimalField(initial=1.99)