from chandelier_web.apps.admin_page_states.models import State
from chandelier_web.apps.admin_page_themes.models import Theme

def themes(request):
    themes = Theme.objects.all()
    return {'themes': themes}

def states(request):
    states = State.objects.all()
    return {'states': states}