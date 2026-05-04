class FormStylingMixin:
    placeholders = {
        'name': 'Введите название товара',
        'description': 'Введите подробное описание',
        'picture': 'Выберете файл',
        'category': 'Выберете категорию',
        'price': 'Введите цену',
    }

    def _apply_common_styles(self):
        for field_name, field in self.fields.items():
            placeholder = self.placeholders.get(field_name, '')  # Получаем подсказку из словаря
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': placeholder
            })