from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'nickname', 'profile_image']
        # description 필드를 선택적으로 설정
        widgets = {
            'description': forms.Textarea(attrs={'required': False}),
        }
