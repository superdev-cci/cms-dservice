from django.forms import ModelForm
from member.models import Member


class CheckInMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['mobile', 'email', 'address', 'amphurid', 'districtid', 'provinceid', 'zip']


