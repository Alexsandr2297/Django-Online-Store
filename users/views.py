from django.urls import reverse_lazy
from django.views.generic import  CreateView
from users.models import User
from users.forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings

class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'user_form.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш магазин'
        message = 'Спасибо, что зарегистрировались в нашем магазине !'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)
