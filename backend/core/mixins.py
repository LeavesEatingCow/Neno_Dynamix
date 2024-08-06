from django.http import Http404

class UserIsOwnerMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            raise Http404
        return obj
