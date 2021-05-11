# from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from .models import User
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordChangeDoneView
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView, UpdateView,DeleteView
# from blog.models import Articles
# from .mixins import FieldMixin, FormValidMixin,AuthorAccessMixin,SuperUserAccessMixin,NoAccessMixin
from account.forms import ProfileForms,SignupForms
from .tokens import account_activation_token


class Profile(LoginRequiredMixin,UpdateView):
    form_class=ProfileForms
    success_url=reverse_lazy('account:profile')
    template_name = 'registration/profile.html'
    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile,self).get_form_kwargs()
        kwargs.update({
        'user':self.request.user
        })
        return kwargs


class Login(LoginView):
    def get_success_url(self):
        user=self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy('stv:home')
        else:
            return reverse_lazy('account:profile')


class Register(CreateView):
    form_class=SignupForms
    template_name="registration/register.html"

    def form_valid(self,form):
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(self.request)
            mail_subject = 'فعال سازی اکانت'
            message = render_to_string('registration/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('لینک فعال سازی به ایمیل شما ارسال شد.')
