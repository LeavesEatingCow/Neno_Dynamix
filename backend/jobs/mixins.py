from django.http import Http404

class ClientIsOwnerMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.client != self.request.user.client:
            raise Http404
        return obj