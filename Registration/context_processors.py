from Registration.models import SiteConfig


def siteconfigs(request):
    all_configs = SiteConfig.objects.all()
    return {
        'configs': all_configs,
    }
