from firebase_admin import auth
from django.http import JsonResponse

class FirebaseAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        id_token = request.headers.get('Authorization')
        if id_token:
            try:
                decoded_token = auth.verify_id_token(id_token)
                request.user = decoded_token
            except:
                return JsonResponse({'error': 'Invalid token'}, status=403)

        response = self.get_response(request)
        return response
