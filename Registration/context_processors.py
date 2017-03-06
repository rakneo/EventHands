from .models import SiteConfigs


def config(request):

    configs = SiteConfigs.objects.all()
    return {
        'config': configs
        }
