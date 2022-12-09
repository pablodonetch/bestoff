from django import forms
from django.core import validators

class formulario_contacto(forms.Form):
    clase='formulario-placeholder form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-orange-600 focus:outline-none'
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':clase, 'placeholder':'Nombre Apellido', 'autocomplete':'off'}))
    email = forms.EmailField(required=False, 
		widget=forms.TextInput(
			attrs={'class': clase, 'placeholder': 'ejemplo@correo.com', 'autocomplete':'off'}
			),
			validators=[
				validators.MinLengthValidator(4, message="El E-Mail es demasiado corto"),
				validators.RegexValidator('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message="El E-Mail ingresado no es válido")
			],
			error_messages={'required':'El campo E-Mail está vacío' }
		)
    telefono = forms.CharField(required=True, widget=forms.TextInput(
			attrs={'class': clase, 'placeholder': '+56912345678', 'autocomplete':'off'}
			),
			validators=[
                validators.MinLengthValidator(6, message="El Teléfono es demasiado corto"),
                validators.RegexValidator('^[+0-9 ]*$', message="El Teléfono contiene caracteres inválidos, por favor use sólo números, por ejemplo +5691652132")
            ]
	)
    mensaje = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':clase, 'placeholder':'¿Qué quieres vender?', 'style': 'height: 140px', 'autocomplete':'off'}))


class formulario_contacto_oferta(forms.Form):
	clase='formulario-placeholder form-control block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-orange-600 focus:outline-none'
	monto = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class':clase, 'placeholder':'Monto de la Oferta en UF', 'autocomplete':'off'}))
	nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':clase, 'placeholder':'Nombre Apellido', 'autocomplete':'off'}))
	email = forms.EmailField(required=True, 
		widget=forms.TextInput(
			attrs={'class': clase, 'placeholder': 'ejemplo@correo.com', 'autocomplete':'off'}
			),
			validators=[
				validators.MinLengthValidator(4, message="El E-Mail es demasiado corto"),
				validators.RegexValidator('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', message="El E-Mail ingresado no es válido")
			],
			error_messages={'required':'El campo E-Mail está vacío' }
		)
	telefono = forms.CharField(required=True, widget=forms.TextInput(
			attrs={'class': clase, 'placeholder': '+56912345678', 'autocomplete':'off'}
			),
			validators=[
                validators.MinLengthValidator(4, message="El Teléfono es demasiado corto"),
                validators.RegexValidator('^[+0-9 ]*$', message="El Teléfono contiene caracteres inválidos, por favor use sólo números, por ejemplo +5691652132")
            ]
	)
	mensaje = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':clase, 'placeholder':'¿Qué quieres vender?', 'style': 'height: 140px', 'autocomplete':'off'}))