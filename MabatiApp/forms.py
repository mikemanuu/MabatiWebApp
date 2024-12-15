from django import forms
from MabatiApp.models import ImageModel, Contact, Product


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'



