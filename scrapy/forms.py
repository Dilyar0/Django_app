from . import parser, models
from django import forms


class ParserForm(forms.Form):
    MEDIA_CHOICE = (
        ("Plants", "Plants"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICE)

    class Meta:
        fields = [
            "media_type",
        ]

    def parse_data(self):
        if self.data["media_type"] == "Plants":
            plant_parser = parser.parser_func()
            for data in plant_parser:
                models.Plant.objects.create(**data)