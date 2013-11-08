__author__ = 'NAV3'
import autocomplete_light
from models import Person

# This will generate a PersonAutocomplete class
autocomplete_light.register(Person,
    # Just like in ModelAdmin.search_fields
    search_fields=['^first_name', 'last_name'],
    # This will actually data-minimum-characters which will set
    # widget.autocomplete.minimumCharacters.
    autocomplete_js_attributes={'placeholder': 'Other model name ?',},
)
