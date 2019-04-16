from crispy_forms.bootstrap import InlineField, FormActions, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


class WineListFormHelper(FormHelper):
    form_id = 'wine-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Wine Records',
                    InlineField('variety'),
                    InlineField('country'),
                    InlineField('province'),
                    InlineField('region_1'),
                    InlineField('region_2'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search',
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )