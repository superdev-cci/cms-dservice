from django.db import models
from django.db.models.signals import post_delete
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from oauth2_provider.models import AccessToken
from Crypto.Cipher import AES


class UserAccount(models.Model):
    crypto = models.BinaryField(max_length=64, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member = models.OneToOneField('member.Member', on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey('branch.Branch', on_delete=models.SET_NULL, null=True, blank=True)
    current_lang = models.CharField(max_length=4, default='TH')
    current_currency = models.CharField(max_length=4, default='BTH')

    mirror_mode = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'User account'

    @property
    def last_login(self):
        return self.user.last_login

    @last_login.setter
    def last_login(self, value):
        self.user.last_login = value
        self.user.save()

    @classmethod
    def get_user_from_access_token(cls, token):
        token = AccessToken.objects.get(token=token)
        if token is not None:
            if hasattr(token.user, 'useraccount'):
                return token.user.useraccount
        return None

    def set_language(self, next):
        self.current_lang = next
        self.save()

    def set_currency(self, next):
        self.current_currency = next
        self.save()

    def set_password(self, password):
        entry = AES.new('asrfdvgrewscxdcc', AES.MODE_CFB, 'zxcvbnmasdfghfvc')
        self.user.set_password(password)
        c_text = entry.encrypt(password)
        self.crypto = c_text
        self.user.save()
        self.save()

    def get_password(self):
        entry = AES.new('asrfdvgrewscxdcc', AES.MODE_CFB, 'zxcvbnmasdfghfvc')
        passwd = entry.decrypt(self.crypto)
        return passwd.decode('utf-8')

    def create_member_account(self, user, password, first_name, last_name, groups='Member'):
        group = Group.objects.get(name=groups)
        try:
            instance = User.objects.create(username=user, first_name=first_name, last_name=last_name, is_active=True)
            self.user = instance
            # Add to group
            instance.groups.add(group)
            # instance.save()
            self.set_password(password)
        except Exception as e:
            return None

        return instance

    def change_user_groups(self, new_groups):
        group = Group.objects.get(name=new_groups)
        self.user.groups.clear()
        self.user.groups.add(group)
        self.user.save()

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.__str__()


@receiver(post_delete, sender=UserAccount)
def user_account_reverse_deleted(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()
    return
