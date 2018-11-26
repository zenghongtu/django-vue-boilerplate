import re
from django.http import response, HttpResponse
from django.views.generic.base import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer

# Serve Vue Application
# index_view = never_cache(TemplateView.as_view(template_name='index.html'))

MOBILE_RE = re.compile(
    '(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino',
    re.I)
TABLET_RE = re.compile(
    '(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino|android|ipad|playbook|silk',
    re.I)


class IndexPageView(TemplateView):
    template_name = 'index.html'

    @never_cache
    def get(self, request, *args, **kwargs):
        _isMobile = self.is_mobile_browser(request)
        if _isMobile:
            self.template_name = 'mobile.html'
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def is_mobile_browser(self, request):
        mobile_browser = False
        ua = request.META['HTTP_USER_AGENT'].lower()
        if MOBILE_RE.search(ua) is not None:
            mobile_browser = True
        return mobile_browser


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


def test(request):
    print(request)
    return HttpResponse('ok')
