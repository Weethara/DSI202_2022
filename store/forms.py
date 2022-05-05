#from django import forms
#from .models import Movie 


# Create your forms here.
#class MovieForm(forms.ModelForm):

#    class Meta:
#        model = Movie
#        fields = ('image')


from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')