from django import forms
from.models import Pizza, Size


# class PizzaForm(forms.Form):
    #type1 & size= 'line'
    #toppins =forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olives','Olives')],widget=forms.CheckboxSelectMultiple)


    # topping1 = forms.CharField(label='Topping1',max_length=100,widget=forms.Textarea)
    # topping2 = forms.CharField(label='Topping2',max_length=100)
    # size = forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])

class PizzaForm(forms.ModelForm):

    # email =forms.EmailField()
    #
    # url = forms.URLField()
    #image = forms.ImageField()
    #size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None,widget=forms.RadioSelect )
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels ={'topping1':'Topping 1','toppings2':'Topping 2'}

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=6)
