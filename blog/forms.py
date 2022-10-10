from cProfile import label
from django import forms
from .models import Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["post"]
        labels = {
            "user_name" : "Your Name",
            "email" : "Your Email",
            "comment" : "Your Comment",
        }
            
    