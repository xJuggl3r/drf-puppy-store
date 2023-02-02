from django.test import TestCase
from ..models import Puppy
from ..serializers import PuppySerializer
from rest_framework import status
from django.test import Client

from django.urls import reverse


class PuppyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Puppy.objects.create(
            name='Rufus', age=5, breed='Labrador', color='Brown')
        Puppy.objects.create(
            name='Rocky', age=4, breed='German Shepherd', color='Black')
        Puppy.objects.create(
            name='Rex', age=1, breed='Pug', color='Brown')

    def test_puppy_breed(self):
        puppy_rufus = Puppy.objects.get(name='Rufus')
        puppy_rocky = Puppy.objects.get(name='Rocky')
        self.assertEqual(
            puppy_rufus.get_breed(), 'Rufus belongs to Labrador breed.')
        self.assertEqual(
            puppy_rocky.get_breed(), 'Rocky belongs to German Shepherd breed.')
