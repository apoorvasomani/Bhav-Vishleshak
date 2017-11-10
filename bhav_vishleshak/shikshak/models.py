from __future__ import unicode_literals

from django.db import models


class DataSet(models.Model):
	"""
	Model that stores the words/phrases

	Fields
	------
	item: Stores the word/phrase
	vector: Accepts -1, 0 and 1 for Negative, Neutral & Postive respectively
	sentiment: Indicates the positivity of the item. Lies between 0 to 1

	"""

	item = models.CharField(max_length=100, unique=True, null=False)
	vector = models.IntegerField(default=0)
	sentiment = models.FloatField( min_value=0, max_value=1)
	