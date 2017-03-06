from .models import SitesConfig


def config(request):

    configs = SiteConfig.objects.all()
    return {
        'config': configs
        }
