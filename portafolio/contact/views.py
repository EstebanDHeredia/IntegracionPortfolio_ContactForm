from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        # ME ESTÁN ENVIANDO LOS DATOS DEL FORMULARIO
        # relleno la variable contact_form con los datos recibidos del request
        contact_form = ContactForm(data=request.POST)

        # print("Datos del form de contacto: {}".format(contact_form))

        if contact_form.is_valid():
            # CAPTURO LOS DATOS DEL request.POST y si no estuvieran los pongo en vacio ""
            name = request.POST.get('name', "")
            email = request.POST.get('email', "")
            message = request.POST.get('message', "")

            # LOGICA DEL ENVIO DEL CORREO ELECTRONICO:
            email = EmailMessage(
                "Mensaje enviado desde la página de contacto",
                "Email enviado por {} <{}>:\n\n{}".format(
                    name, email, message),
                email,
                ['4bb3ea2186761d@inbox.mailtrap.io'],
                reply_to=[email]
            )

            try:
                email.send()
                # con la siguiente linea y el ok que le envío lo que hago es confirmarle al usuario que el mensaje se envió correctamente
                # PODRIA HABER PUESTO return redirect('/contact/?ok') PERO ASÍ ESTARIA HARDCODEANDO LA URL, USANDO REVERSE, PERMITO QUE SI SE CAMBIA LA URL EL PROYECTO SIGA FUNCIONANDO
                return redirect(reverse('contact')+'?ok')

            except:
                # FALLO AL ENVIAR EMAIL
                return redirect(reverse('contact')+'?error')

    return render(request, 'contact/contact.html', {'form': contact_form})
