from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .services import CandidateService

class CandidateView(APIView):
    def post(self, request):
        candidate, errors, created = CandidateService.create_or_update_candidate(request.data)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'message': 'Candidate created successfully' if created else 'Candidate updated successfully',
            'candidate_id': candidate.id
        }, status= status.HTTP_201_CREATED if created else status.HTTP_200_OK)
