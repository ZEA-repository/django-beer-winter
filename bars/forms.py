from django import forms

from bars.models import Bar


class BarForm(forms.ModelForm):
	class Meta:
		model = Bar
		fields = [
			"title",
		]
