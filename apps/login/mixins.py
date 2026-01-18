from django.shortcuts import redirect


class JWTLoginRequiredMixin:
    login_url = "registratsiya:login"

    def dispatch(self, request, *args, **kwargs):
        # middleware qo‘ygan user_jwt
        if not getattr(request, "user_jwt", None):
            return redirect(self.login_url)

        return super().dispatch(request, *args, **kwargs)
