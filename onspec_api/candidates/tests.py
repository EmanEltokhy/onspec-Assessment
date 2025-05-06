from django.test import TestCase
from .models import Candidate
from .services import CandidateService

class CandidateModelTest(TestCase):
    def test_create_candidate(self):
        candidate = Candidate.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com"
        )
        self.assertEqual(candidate.first_name, "John")
        self.assertEqual(candidate.email, "john.doe@example.com")

class CandidateServiceTest(TestCase):
    def test_create_candidate(self):
        data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com'
        }
        candidate, errors, created = CandidateService.create_or_update_candidate(data)
        self.assertIsNotNone(candidate)
        self.assertIsNone(errors)
        self.assertTrue(created)
        self.assertEqual(candidate.email, 'jane.smith@example.com')

    def test_update_candidate(self):
        # First create
        data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com'
        }
        candidate, _, _ = CandidateService.create_or_update_candidate(data)
        
        # Then update
        update_data = {
            'first_name': 'Jane',
            'last_name': 'Smith-Jones',
            'email': 'jane.smith@example.com',
            'phone_number': '1234567890'
        }
        updated_candidate, errors, created = CandidateService.create_or_update_candidate(update_data)
        self.assertIsNotNone(updated_candidate)
        self.assertIsNone(errors)
        self.assertFalse(created)
        self.assertEqual(updated_candidate.last_name, 'Smith-Jones')
        self.assertEqual(updated_candidate.phone_number, '1234567890')