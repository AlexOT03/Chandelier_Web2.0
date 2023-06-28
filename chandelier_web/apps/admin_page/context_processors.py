from chandelier_web.apps.home_page.models import Message

def messages(request):
    messages = Message.objects.all()
    return {'messages': messages}
