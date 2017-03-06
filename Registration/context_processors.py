from .models import SiteConfig


def config(request):

    configs = SiteConfig.objects.all()
    return {
        'config': configs
        }
