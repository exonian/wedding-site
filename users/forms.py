from mezzanine.accounts.forms import ProfileForm
from django.contrib.auth import get_user_model

class UserForm(ProfileForm):

    class Meta:
        model = get_user_model()
        fields = ("email",)
