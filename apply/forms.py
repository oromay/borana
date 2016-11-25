from django import forms
from .models import Apply
from multiupload.fields import MultiFileField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML, Field
from crispy_forms.bootstrap import (
    PrependedText,
    PrependedAppendedText,
    FormActions
)

class ApplyForm(forms.ModelForm):
    attachments = MultiFileField(label = "Обоснование проекта, резюме, смета, рекомендации", min_num=1, max_num=5)
    email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(Fieldset(
        "Вы можете отправить заявку на адрес <a scr='mailto:oromay@yandex.ru'>oromay@yandex.ru</a> или воспользовавшись формой:",
        'second_name',
        'first_name',
        'email',
        HTML("""
        <p>Пожалуйста, используйте текстовые форматы (rtf, doc/docx, odt). Вы можете отправит файлы по-отедльности или объединить их в несколько документов (файл с Вашим проектом желательно оставить анонимным).</p>
        """),
        Field('attachments', css_class='file', type='file', data_show_upload="false"), HTML("{% csrf_token %}"),
        FormActions(Submit('purchase', 'ОТПРАВИТЬ', css_class='btn-primary btn-block'))
        ))
    class Meta:
        model = Apply
        fields = [
        "first_name",
        "second_name",
        "email",
        "attachments",
        ]
