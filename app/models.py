from dynamorm import DynaModel
from marshmallow import fields
from django.conf import settings


class MyTable(DynaModel):
	class Table:
		resource_kwargs = {
			'endpoint_url': settings.DB_ENDPOINT
		}
		name = settings.DB_TABLE
		hash_key = 'created_on'
		read = 25
		write = 5

	class Schema:
		name = fields.String()
		diet = fields.String()
		email = fields.Email()
		created_on = fields.DateTime()



DIET_CHOICES = [('', 'choose diet'), ('gluten-free', 'gluten-free'), ('Keto', 'Keto'), ('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan')]
