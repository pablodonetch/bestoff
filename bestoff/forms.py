from django import forms
from django.core import validators

class formulario_buscar(forms.Form):
	contrato_vigente = forms.BooleanField(required=True, )
	comuna=forms.CharField(required=True,
		widget=forms.TextInput(attrs={'class':'col-span-12 md:col-span-7 mr-1 my-2 rounded-md bg-gray-50 border border-gray-300 text-gray-900 text-sm sm:text-base focus:ring-orange-500 focus:border-orange-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-orange-500 dark:focus:border-orange-500','id':'Comuna', 'placeholder':'Ingresa la Comuna...'}))


class formulario_contacto(forms.Form):
    clase='block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-gray-700 focus:outline-none'
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

class formulario_vender(forms.Form):
	clase=" text-black placeholder-gray-600 w-full px-4 py-2.5 mt-2 text-base   transition duration-500 ease-in-out transform border-transparent rounded-lg bg-gray-200  focus:border-blueGray-500 focus:bg-white dark:focus:bg-gray-800 focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2 ring-gray-400"
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
	telefono = forms.CharField(required=True, 
		widget=forms.TextInput(
			attrs={'class': clase, 'placeholder': '+56912345678', 'autocomplete':'off'}
			),
			validators=[
                validators.MinLengthValidator(6, message="El Teléfono es demasiado corto"),
                validators.RegexValidator('^[+0-9 ]*$', message="El Teléfono contiene caracteres inválidos, por favor use sólo números, por ejemplo +5691652132")
            ]
	)
	comuna=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':clase, 'placeholder':'Comuna', 'autocomplete':'off'}))
	direccion=forms.CharField(required=True, widget=forms.TextInput(attrs={'class':clase, 'placeholder':'Dirección', 'autocomplete':'off'}))
	caracteristicas=forms.CharField(required=True, widget=forms.Textarea(attrs={'class':clase, 'placeholder':'¿Qué quieres vender?', 'style': 'height: 140px', 'autocomplete':'off'}))


class formulario_contacto_oferta(forms.Form):
	clase='block w-full px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-orange-600 focus:outline-none'
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
	forma_pago = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':clase, 'placeholder':'Forma de Pago (ej: crédito hipotecario)',  'autocomplete':'off'}))

class formulario_contacto_oferta_2(forms.Form):
	clase=" text-black placeholder-gray-600 w-full px-4 py-2.5 mt-2 text-base   transition duration-500 ease-in-out transform border-transparent rounded-lg bg-gray-200  focus:border-blueGray-500 focus:bg-white dark:focus:bg-gray-800 focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2 ring-gray-400"
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
	forma_pago = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':clase, 'placeholder':'Forma de Pago (ej: crédito hipotecario)',  'autocomplete':'off'}))

class formulario_financiero(forms.Form):
	#clase='block w-full px-3 py-0.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-orange-600 focus:outline-none'
	clase=" text-black placeholder-gray-600 w-full px-4 py-0.5 mt-2 text-base transition duration-500 ease-in-out transform border-transparent rounded-lg bg-gray-200  focus:border-blueGray-500 focus:bg-white dark:focus:bg-gray-800 focus:outline-none focus:shadow-outline focus:ring-2 ring-offset-current ring-offset-2 ring-gray-400"
	precio_compra = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class':clase, 'autocomplete':'off'}))
	pie=forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class':clase, 'autocomplete':'off'}))
	tasa= forms.CharField(required=True, widget=forms.TextInput(attrs={'class':clase, 'autocomplete':'off'}))
	arriendo_esperado=forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class':clase, 'autocomplete':'off'}))
	