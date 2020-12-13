import json

from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView

# setup()
# dispatch()
# http_method_not_allowed()
# get_template_names()
# get_slug_field()
# get_queryset()
# get_object()
# get_context_object_name()
# get_context_data()
# get()
# render_to_response()


class AlbumView(BaseDetailView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hello"] = "world"
        return context

    def get_object(self):
        return None

    def render_to_response(self, context):
        return JsonResponse({"hell": "world"})
