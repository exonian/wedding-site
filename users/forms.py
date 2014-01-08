from mezzanine.accounts.forms import ProfileForm
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from templated_email import send_templated_mail

class UserForm(ProfileForm):

    class Meta:
        model = get_user_model()
        fields = ("email",)

    def clean(self):
        self.had_email = bool(self.instance.email)
        return super(UserForm, self).clean()

    def save(self, *args, **kwargs):
        user = super(UserForm, self).save()
        if user.email and 'email' in self.changed_data:
            self.send_emails(user)
        return user

    def send_emails(self, user, *args, **kwargs):
        context = {
            'user': user,
            'had_email': self.had_email,
            'site': Site.objects.get_current(),
        }
        # to the user
        send_templated_mail(
            template_name='users/email-address',
            from_email='wedding@michaelblatherwick.co.uk',
            recipient_list=[user.email],
            context=context,
        )
        # to us
        send_templated_mail(
            template_name='users/email-address-notification',
            from_email='wedding@michaelblatherwick.co.uk',
            recipient_list=['wedding@michaelblatherwick.co.uk'],
            context=context,
        )
