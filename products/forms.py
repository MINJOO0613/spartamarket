from django import forms
from .models import Product, Comment


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {'price': forms.NumberInput(attrs={'step': 500}),}
        exclude = ('author', 'like_users', 'views')
        
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("0원 미만은 입력할 수 없습니다.")
        return price


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("product","user")