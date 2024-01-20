from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView Feature"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, pathc, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your applicaiton login',
            'Is mapped manually to URLs'
        ]
        
        return Response({'message': 'Hello!', 'an_aipview': an_apiview})

    