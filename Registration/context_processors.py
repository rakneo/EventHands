from .models import SiteSettings


def config(request):

    configs = SiteSettings.objects.all()
    return {
        'config': configs
        }
