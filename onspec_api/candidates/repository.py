from .models import Candidate

class CandidateRepository:
    @staticmethod
    def get_by_email(email):
        try:
            return Candidate.objects.get(email=email)
        except Candidate.DoesNotExist:
            return None

    @staticmethod
    def create_candidate(candidate_data):
        return Candidate.objects.create(**candidate_data)

    @staticmethod
    def update_candidate(candidate, candidate_data):
        updated = False
        for field, value in candidate_data.items():
            if getattr(candidate, field) != value:
                setattr(candidate, field, value)
                updated = True
        if updated:
            candidate.save()
        return candidate
