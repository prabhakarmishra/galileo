"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from Xploora.alpha.models import Item
import logging

logger = logging.getLogger('alpha')

class SimpleTest(TestCase):
    def test_item_id(self, item_id=102):
        logger.debug('Good!')
        print Item.objects.get(pk=item_id)

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
