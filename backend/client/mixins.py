from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class ClientAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an interpreter."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_client:
            return redirect("core:login")
        return super().dispatch(request, *args, **kwargs)