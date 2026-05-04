from django import forms
from .models import Product
from django.core.exceptions import ValidationError
from .form_mixin import FormStylingMixin


class ProductForm(FormStylingMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'picture', 'category', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_common_styles()

    def clean(self):
        listing = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for i in listing:
            if i in name.lower():
                raise ValidationError("Запрещенное слово в названии")
            if i in description.lower():
                raise ValidationError("Запрещенное слово в описании")
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price is not None and price != '':
            price = float(price)
            if price <= 0:
                raise ValidationError("Цена не может быть отрицательной")

        return price

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            if picture.size > 5 * 1024 * 1024:  # Проверка на размер > 5MB
                raise ValidationError("Размер изображения не должен превышать 5MB.")
            if picture.image.format not in ['JPEG', 'PNG']:
                raise ValidationError("Изображение должно быть в формате JPEG или PNG.")
        return picture
