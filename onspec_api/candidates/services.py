from .repository import CandidateRepository
from .serializers import CandidateSerializer

class CandidateService:
    @staticmethod
    def create_or_update_candidate(data):
        email = data.get('email')
        candidate = CandidateRepository.get_by_email(email)
        created = False
        
        if candidate:
            serializer = CandidateSerializer(candidate, data=data, partial=True)
        else:
            serializer = CandidateSerializer(data=data)
        
        if serializer.is_valid():
            if candidate:
                candidate = CandidateRepository.update_candidate(candidate, serializer.validated_data)
            else:
                candidate = CandidateRepository.create_candidate(serializer.validated_data)
                created = True
            return candidate, None, created
        return None, serializer.errors, None
