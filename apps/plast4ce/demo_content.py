"""Single-item lists for Plast4ce templates until CMS models are wired."""

SITE_NAME = 'Sahel Plast4ce'
TAGLINE = 'Sahel Recycling & Sustainability'

SERVICE_ITEMS = [
    {
        'id': 1,
        'title': 'Plastic recovery & reprocessing',
        'excerpt': 'Collection, sorting, and channeling post-consumer plastics into verified recycling streams.',
        'image': 'plast4ce/img/service/service_1.jpg',
        'list_icon': 'plast4ce/img/service/bottle.png',
        'thumb': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'hero_image': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'body': (
            f'{SITE_NAME} partners with municipalities and industry to keep plastics in the circular economy—'
            'with traceable handling and reporting you can stand behind.'
        ),
    },
]

PROJECT_ITEMS = [
    {
        'id': 1,
        'title': 'Regional MRF upgrade',
        'image': 'plast4ce/img/project/1.jpg',
        'excerpt': 'Sorting line modernization that improved capture rates for recyclables.',
        'body': (
            'A representative program showing how Sahel Plast4ce aligns equipment, training, and data for lasting diversion gains.'
        ),
    },
]

BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Why traceability matters in plastic recycling.',
        'excerpt': 'Stakeholders expect proof—not promises—when reporting diversion and carbon benefits.',
        'author': 'Sahel Plast4ce',
        'date_display': '12 Apr 2024',
        'image': 'plast4ce/img/blog/1.jpg',
    },
]

TEAM_MEMBERS = [
    {
        'id': 1,
        'name': 'Kemi Adeyemi',
        'role': 'Head of circular programs',
        'image': 'plast4ce/img/team/1.jpg',
        'bio': (
            'Kemi leads collection partnerships and processor relationships for Sahel Plast4ce across the region.'
        ),
    },
]

SHOP_PRODUCTS = [
    {
        'id': 1,
        'title': 'Recycling starter kit (demo SKU)',
        'price': '$89.00',
        'price_old': '$99.00',
        'image': 'plast4ce/img/blog/lp-1-1.jpg',
        'detail_image': 'plast4ce/img/blog/blog-details-img.jpg',
        'excerpt': 'Representative product for storefront demos—replace with live catalog later.',
    },
]


def get_by_id(items, pk):
    for item in items:
        if item['id'] == int(pk):
            return item
    return None
