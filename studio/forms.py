
from django import forms

from .models import Enquiry, ContactServiceOption


class EnquiryForm(forms.ModelForm):

    service = forms.ChoiceField(
        choices=[],
        required=True,
        widget=forms.Select(attrs={
            "class": "contact-select"
        })
    )

    class Meta:
        model = Enquiry

        fields = [
            "name",
            "email",
            "phone",
            "service",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your name"
            }),

            "email": forms.EmailInput(attrs={
                "placeholder": "you@example.com"
            }),

            "phone": forms.TextInput(attrs={
                "placeholder": "+91 98765 43210"
            }),

            "message": forms.Textarea(attrs={
                "placeholder": "Tell us about your project",
                "rows": 5
            }),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        active_services = ContactServiceOption.objects.filter(
            is_active=True
        ).order_by(
            "sort_order",
            "id"
        )

        self.fields["service"].choices = [
            ("", "Select a service")
        ] + [
            (option.value, option.label)
            for option in active_services
        ]

        self.fields["service"].error_messages["required"] = (
            "Please select a service."
        )

