from django.forms import ModelForm
from django import forms
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from bootstrap3_datetime.widgets import DateTimePicker

# class ReferralForm(ModelForm):
#     class Meta:
#         model = models.Referral
#         exclude = ['patient', 'author',
#                    'author_type', 'written_datetime',
#                    'last_modified', 'referral_status']

#     def __init__(self, *args, **kwargs):
#         super(ReferralForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.add_input(Submit('submit', 'Add referral followup'))

class SpecialtyReferralForm(ModelForm):
    class Meta:
        model = models.SpecialtyReferral
        exclude = ['patient', 'author',
                   'author_type', 'written_datetime',
                   'last_modified', 'referral_status']

    def __init__(self, *args, **kwargs):
        super(SpecialtyReferralForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Add referral followup'))

class FQHCReferralForm(ModelForm):
    class Meta:
        model = models.FQHCReferral
        exclude = ['patient', 'author',
                   'author_type', 'written_datetime',
                   'last_modified', 'referral_status']

    def __init__(self, *args, **kwargs):
        super(FQHCReferralForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Add referral followup'))

class FollowupRequestForm(ModelForm):
    class Meta:
        model = models.FollowupRequest
        exclude = ['patient', 'author',
                   'author_type', 'written_datetime',
                   'last_modified', 'completion_date',
                   'completion_author', 'referral']
        widgets = {'due_date': DateTimePicker(options={"format": "YYYY-MM-DD",
                                                       "pickTime": False})}

    def __init__(self, *args, **kwargs):
        super(FollowupRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

class PatientContactForm(ModelForm):
    class Meta:
        model = models.PatientContact
        exclude = ['referral', 'followupRequest', 'patient',
                   'author', 'author_type']

    def __init__(self, *args, **kwargs):
        super(PatientContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

class ReferralSelectForm(forms.Form):
    referrals = forms.ModelChoiceField(queryset=models.Referral.objects.all())

    def __init__(self, *args, **kwargs):
        super(ReferralSelectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))