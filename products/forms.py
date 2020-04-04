from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title","class":"form-control"}))
  #  email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
                                    attrs=
                                    {"class":"form-control",
                                    "placeholder":"Your Description",
                                    "id":"123",
                                    "rows":15}))
    price = forms.DecimalField(initial=1)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

   # def clean_title(self, *args, **kwargs):
    #    title = self.cleaned_data.get("title")
    #    if not "CFE" in title:
   #         raise forms.ValidationError("This is not a valid title.")
   #     return title

  #  def clean_email(self, *args, **kwargs):
  #      email = self.cleaned_data.get("email")
   #     if not email.endswith("edu"):
   #         raise forms.ValidationError("This is not a valid email.")
    #    return email
            

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"Your Title","class":"form-control"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
                                    attrs=
                                    {"class":"form-control",
                                    "placeholder":"Your Description",
                                    "id":"123",
                                    "rows":15}))
    price = forms.DecimalField(initial=1)