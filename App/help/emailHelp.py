# Email Config
from BlankSetup import settings
HOST_USER = settings.EMAIL_HOST_USER
from django.core.mail import BadHeaderError, EmailMessage, EmailMultiAlternatives, send_mail, send_mass_mail


def SendOneToOneEmail(subject, message, to):
    send_mail('subject', 'message', HOST_USER, to, fail_silently = False)
    print("DDv")


def SendMassEmail():
    message1 = ('Subject here', 'Here is the message', 'from@example.com', ['first@example.com', 'other@example.com'])
    message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
    send_mass_mail((message1, message2), fail_silently=False)

    datatuple = (
                    ('Subject', 'Message.', 'from@example.com', ['john@example.com']),
                    ('Subject', 'Message.', 'from@example.com', ['jane@example.com']),
                )
    send_mass_mail(datatuple)


def SendMultiPartEmail():
    subject, from_email, to = 'hello', HOST_USER, 'kuntal.samanta@cbnits.com'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p> \
        <img src="https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072823_960_720.jpg">'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()