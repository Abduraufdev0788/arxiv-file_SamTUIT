from django.shortcuts import redirect
from django.http import HttpResponseForbidden


class JWTLoginRequiredMixin:
    login_url = "registratsiya:login"

    def dispatch(self, request, *args, **kwargs):
        # middleware qo‘ygan user_jwt
        if not getattr(request, "user_jwt", None):
            return redirect(self.login_url)

        return super().dispatch(request, *args, **kwargs)
    
class AdminOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        user = getattr(request, "user_jwt", None)

        if not user:
            return redirect("login")

        if user.role != "Admin":
            return HttpResponseForbidden("Bu admin panel ❌")

        return super().dispatch(request, *args, **kwargs)
