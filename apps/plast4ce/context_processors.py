from apps.plast4ce.demo_content import SITE_NAME, TAGLINE


def site(request):
    return {
        'site_name': SITE_NAME,
        'division_tagline': TAGLINE,
    }
