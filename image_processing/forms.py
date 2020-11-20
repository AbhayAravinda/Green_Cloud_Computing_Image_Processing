from django import forms

img_choices = (("grayscale", "grayscale"), ("histogram", "histogram"),
               ("gaussian_blur", "gaussian_blur"), ("brightness_increase", "brightness_increase"), ("brightness_decrease", "brightness_decrease"), ("color_inversion", "color_inversion"), ("negative_image", "negative_image"), ("sepia", "sepia"), ("clahe", "clahe"))


class imageForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'hide_file', 'id': 'myFile', 'onchange': "readURL(this)", 'name': "filename"}))
    option = forms.ChoiceField(choices=img_choices)
