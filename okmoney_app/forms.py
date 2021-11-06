from django import forms
from django.db.models import fields
from . import models
from logging import PlaceHolder

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Layout, Column, HTML, Submit, Div


class MoneyForm(forms.ModelForm):
    date = forms.DateField(
        required=True,
        label='Data ',
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            attrs={
                'class': 'mydatepicker',
                'placeholder': 'Data',
            }
        )
    )

    operation = forms.ChoiceField(
        initial='Não informado',
        required=True,
        label='Operação Financeira ',
        choices=[
            ('entrada', 'Entrada Financeira'),
            ('saida', 'Saída Financeira'),
        ],
    )

    reason = forms.CharField(
        max_length=200,
        required=True,
        label='Motivo ',
        widget=forms.TextInput(attrs={'placeholder': 'Motivo'}),
    )

    place = forms.CharField(
        max_length=200,
        required=False,
        label='Local ',
        widget=forms.TextInput(attrs={'placeholder': 'Local'}),
    )

    value = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        label='Valor (R$) ',
        widget=forms.NumberInput(attrs={'placeholder': 'Valor'}),
    )

    payment_method = forms.ChoiceField(
        initial='Não informado',
        required=True,
        label='Método ',
        choices=[
            ('dinheiro', 'Dinheiro'),
            ('card_d', 'Cartão de Débito'),
            ('card_c', 'Cartão de Crédito'),
            ('pix', 'PIX'),
            ('transferencia', 'Transferência'),
            ('deposito', 'Depósito'),
        ],
    )

    observation = forms.CharField(
        max_length=200,
        required=False,
        label='Observação',
        widget=forms.Textarea(attrs={'placeholder': 'Observação'}),
    )

    class Meta:
        model = models.MoneyReleases
        fields = ['date', 'operation', 'reason', 'place', 'value',
                  'payment_method', 'observation']

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(MoneyForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Column('date', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('operation', css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Column('reason', css_class='col-md-8'),
                css_class='row'
            ),
            Div(
                Column('place', css_class='col-md-8'),
                css_class='row'
            ),
            Div(
                Column('value', css_class='col-md-4'),
                css_class='row'
            ),
            Div(
                Column('payment_method', css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Column('observation', css_class='col-md-11'),
                css_class='row'
            ),
            ButtonHolder(
                HTML(
                    '<a class="btn mb-1 btn-rounded btn-warning" href="{% url "releases" %}" type="button">Cancelar</a>'
                ),
                Submit('submit', 'Salvar',
                       css_class='btn mb-1 btn-rounded btn-success'),
            )
        )
