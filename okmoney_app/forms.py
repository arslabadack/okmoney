from . import models
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Layout, Column, HTML, Submit, Div


class MoneyInModelForm(forms.ModelForm):
    date = forms.DateField(
        required=True,
        label='Data ',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={
                'class': '.datepicker',
                'type': 'date',
                'placeholder': 'dd/mm/aaaa',
                'todayBtn': 'linked',
            }
        )
    )

    category = forms.ChoiceField(
        initial='',
        required=True,
        label='Categoria de Entrada',
        choices=[
            ('', 'Selecione a Operação'),
            ('salario', 'Salário'),
            ('decimo', 'Décimo Terceiro'),
            ('ferias', 'Férias'),
            ('abono', 'Abonos e Comissões'),
            ('outros', 'Outros'),
        ],
    )

    value = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        label='Valor (R$) ',
        widget=forms.NumberInput(attrs={'placeholder': 'Valor'}),
    )

    observation = forms.CharField(
        max_length=200,
        required=False,
        label='Observação',
        widget=forms.Textarea(attrs={'placeholder': 'Observação'}),
    )

    class Meta:
        model = models.MoneyIn
        fields = ['date', 'category', 'value', 'observation']

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(MoneyInModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Column('category', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('value', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('date', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('observation', css_class='col-md-6'),
                css_class='row'
            ),
            ButtonHolder(
                HTML(
                    '<a class="btn mb-1 btn-rounded btn-danger" href="{% url "index" %}" type="button">Cancelar</a>'
                ),
                Submit('submit', 'Salvar',
                       css_class='btn mb-1 btn-rounded btn-success'),
            )
        )


class MoneyOutModelForm(forms.ModelForm):
    date = forms.DateField(
        required=True,
        label='Data ',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={
                'class': '.datepicker',
                'type': 'date',
                'placeholder': 'dd/mm/aaaa',
                'todayBtn': 'linked',
            }
        )
    )

    category = forms.ChoiceField(
        initial='',
        required=True,
        label='Categoria de Custo ',
        choices=[
            ('', 'Selecione a Operação'),
            ('saude', 'Higiene e Saúde'),
            ('alimentacao', 'Alimentação'),
            ('lazer', 'Lazer'),
            ('entretenimento', 'Entretenimento'),
            ('energiasaneamento', 'Energia/Saneamento'),
            ('impostos', 'Encargos/Impostos'),
            ('combustivel', 'Combustível'),
            ('outros', 'Outros'),
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
        required=True,
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
        initial='',
        required=True,
        label='Método ',
        choices=[
            ('', 'Selecione o Método'),
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
        model = models.MoneyOut
        fields = ['date', 'category', 'reason', 'place', 'value',
                  'payment_method', 'observation']

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(MoneyOutModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Column('reason', css_class='col-md-3'),
                Column('category', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('place', css_class='col-md-3'),
                Column('date', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('value', css_class='col-md-3'),
                Column('payment_method', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('observation', css_class='col-md-6'),
                css_class='row'
            ),
            ButtonHolder(
                HTML(
                    '<a class="btn mb-1 btn-rounded btn-danger" href="{% url "index" %}" type="button">Cancelar</a>'
                ),
                Submit('submit', 'Salvar',
                       css_class='btn mb-1 btn-rounded btn-success'),
            )
        )


class FutureModelForm(forms.ModelForm):
    release_date = forms.DateField(
        required=True,
        label='Data de Lançamento ',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={
                'class': '.datepicker',
                'type': 'date',
                'placeholder': 'dd/mm/aaaa',
                'todayBtn': 'linked',
            }
        )
    )

    receiving_date = forms.DateField(
        required=True,
        label='Data de Recebimento ',
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            attrs={
                'class': '.datepicker',
                'type': 'date',
                'placeholder': 'dd/mm/aaaa',
                'todayBtn': 'linked',
            }
        )
    )

    category = forms.ChoiceField(
        initial='',
        required=True,
        label='Operação ',
        choices=[
            ('', 'Selecione a Operação'),
            ('entrada', 'Crédito (recebimento)'),
            ('saida', 'Débito (dívida)'),
        ],
    )

    reason = forms.CharField(
        max_length=300,
        required=True,
        label='Motivo ',
        widget=forms.TextInput(attrs={'placeholder': 'Motivo'}),
    )

    value = forms.DecimalField(
        max_digits=8,
        decimal_places=2,
        required=True,
        label='Valor (R$) ',
        widget=forms.NumberInput(attrs={'placeholder': 'Valor'}),
    )

    class Meta:
        model = models.Future
        fields = ['release_date', 'receiving_date',
                  'category', 'reason', 'value']

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(FutureModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Column('release_date', css_class='col-md-3'),
                Column('receiving_date', css_class='col-md-3'),
                Column('category', css_class='col-md-3'),
                css_class='row'
            ),
            Div(
                Column('reason', css_class='col-md-6'),
                Column('value', css_class='col-md-3'),
                css_class='row'
            ),
            ButtonHolder(
                HTML(
                    '<a class="btn mb-1 btn-rounded btn-danger" href="{% url "index" %}" type="button">Cancelar</a>'
                ),
                Submit('submit', 'Salvar',
                       css_class='btn mb-1 btn-rounded btn-success'),
            )
        )


class RemindersModelForm(forms.ModelForm):

    content = forms.CharField(
        required=False,
        max_length=500,
        label='',
        widget=forms.TextInput(
            attrs={'placeholder': 'Digite seu lembrete aqui'}),
    )

    class Meta:
        model = models.Reminders
        fields = ['content']

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned = self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(RemindersModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Div(
                Column('content', css_class='col-11'),
                css_class='row'
            ),
        )
