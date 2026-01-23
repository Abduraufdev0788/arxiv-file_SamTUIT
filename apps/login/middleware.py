from .jwt_utils import decode_token
from .models import Registration


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user_jwt = None

        token = request.COOKIES.get("access_token")
        if token:
            payload = decode_token(token)
            if payload:
                user = Registration.objects.filter(
                    id=payload["user_id"]
                ).first()
                request.user_jwt = user

        return self.get_response(request)
