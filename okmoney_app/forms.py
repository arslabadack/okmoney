from django import forms
from django.db.models import fields
from . import models
from logging import PlaceHolder

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Layout, Column, HTML, Submit, Div


class MoneyInForm(forms.ModelForm):
    data = forms.DateField(
        required=True,
        label='Data',
        widget=forms.widgets.DateInput(attrs={'type': 'date'})
    )

    categoria = forms.CharField(
        max_length=100,
        required=True,
        label='Categoria',
        widget=forms.TextInput(attrs={'placeholder': 'Categoria'}),
    )

    valor = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        label='Valor',
        widget=forms.NumberInput(attrs={'placeholder': 'Valor'}),
    )

    observacao = forms.CharField(
        max_length=200,
        required=False,
        label='Observação',
        widget=forms.Textarea(attrs={'placeholder': 'Observação'}),
    )

    class Meta:
        model = models.MoneyIn
        fields = ['data', 'categoria', 'valor', 'observacao']

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(MoneyInForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Column('data', css_class='col-md-2'),
                css_class='row'
            ),
            Div(
                Column('categoria', css_class='col-md-6'),
                css_class='row'
            ),
            Div(
                Column('valor', css_class='col-md-4'),
                css_class='row'
            ),
            Div(
                Column('observacao', css_class='col-lg-6'
                       ),
                css_class='row'
            ),
            ButtonHolder(
                HTML(
                    '<a class="btn btn-danger m-3" href="{% url "index" %}" type="button">Cancelar</a>'
                ),
                Submit('submit', 'Salvar', css_class='float-end'),
            )
        )


class MoneyOutForm(forms.ModelForm):
    data = forms.DateField(
        required=True,
        label='Data',
        widget=forms.SelectDateWidget)

    motivo = forms.CharField(
        max_length=200,
        required=True,
        label='Motivo',
        widget=forms.TextInput(attrs={'placeholder': 'Motivo'}),
    )

    local = forms.CharField(
        max_length=200,
        required=True,
        label='Local',
        widget=forms.TextInput(attrs={'placeholder': 'Local'}),
    )

    valor = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        label='Valor',
        widget=forms.NumberInput(attrs={'placeholder': 'Valor'}),
    )

    metodo_pagamento = forms.CharField(
        max_length=100,
        required=True,
        label='Metodo de Pagamento',
        widget=forms.Textarea(attrs={'placeholder': 'Metodo de Pagamento'}),
    )

    observacao = forms.CharField(
        max_length=200,
        required=False,
        label='Observação',
        widget=forms.Textarea(attrs={'placeholder': 'Observação'}),
    )

    class Meta:
        model = models.MoneyOut
        fields = ['data', 'motivo', 'local', 'valor',
                  'metodo_pagamento', 'observacao']

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(MoneyOutForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Column(
                    'data',
                    'motivo',
                    'local',
                    'valor',
                    'metodo_pagamento',
                    'observacao',
                    css_class='col-lg-8'
                ),
                css_class='row'
            ),
            ButtonHolder(
                Submit('submit', 'Salvar', css_class='btn-primary')
            )
        )
