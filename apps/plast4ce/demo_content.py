"""Site copy sourced from SAHEL-Plast4CE company profile (PDF)."""

SITE_NAME = 'Sahel Plast4CE'
TAGLINE = 'Plastics for circular economy'

PARENT_COMPANY = 'SAHEL Enerlog Services Limited'
COMPANY_WEBSITE_LABEL = 'www.sahelenerlog.com'
COMPANY_WEBSITE_URL = 'https://www.sahelenerlog.com'

CONTACT_ADDRESS = 'Gombe Industrial Park, Gombe State, Nigeria'
CONTACT_PHONE_DISPLAY = '+234 806 776 6435'
CONTACT_PHONE_TEL = '+2348067766435'

COMPANY_PROFILE_PDF = 'plast4ce/documents/SAHEL-Plast4CE-Profile.pdf'

HERO_SUBTITLE = (
    'Industrial-scale recycling aligned with Nigeria’s plastic waste policy and NDCs—'
    'from community collection in Gombe and Taraba to traceable PET and PP recyclate.'
)

HERO_SLIDES = [
    {
        'image': 'plast4ce/img/carousel_slides/1.jpg',
        'eyebrow': SITE_NAME,
        'title': TAGLINE,
        'subtitle': HERO_SUBTITLE,
        'cta_label': 'Learn more',
        'cta_url_name': 'plast4ce:plast4ce_about',
    },
    {
        'image': 'plast4ce/img/carousel_slides/2.jpg',
        'eyebrow': 'Collection & processing',
        'title': 'From waste to raw material',
        'subtitle': (
            'PET and PP bales, washed flakes, and a roadmap to rPET and rPP pellets—supplied to converters '
            'with traceable flows.'
        ),
        'cta_label': 'Our services',
        'cta_url_name': 'plast4ce:plast4ce_services',
    },
    {
        'image': 'plast4ce/img/carousel_slides/3.jpg',
        'eyebrow': 'Gombe & Taraba',
        'title': 'Community-first recycling',
        'subtitle': (
            'Fair pricing for reclaimers, cluster programmes, and logistics strength from SAHEL Enerlog—'
            'built for scale across Nigeria.'
        ),
        'cta_label': 'Contact us',
        'cta_url_name': 'plast4ce:plast4ce_contact',
    },
]

HOME_ABOUT_LABEL = 'Circular plastics & industrial value'
HOME_ABOUT_TITLE = 'Sahel Plast4CE at a glance'
HOME_ABOUT_HIGHLIGHT = (
    'We turn plastic waste into new value for industry and communities—as the circular economy unit of '
    f'{PARENT_COMPANY}, backed by logistics, haulage, and port infrastructure experience.'
)
HOME_ABOUT_BODY = (
    'Operations start in Gombe and Taraba States and are designed to scale across Nigeria: '
    'collection and baling, community reclaimers networks, washing and flaking, with a roadmap to '
    'rPET and rPP pellets for converters and EPR partners.'
)

# YouTube “watch” URL: youtube.com/watch?v=XXXXXXXXXXX — use the 11-character XXXXXXXXXXX here.
# Leave empty ('') to show the static image instead of a player.
HOME_ABOUT_YOUTUBE_VIDEO_ID = ''

ABOUT_INTRO = (
    f'At {SITE_NAME}, we turn plastic waste into new value for industry and communities. '
    f'We are the circular economy business unit of {PARENT_COMPANY}, an indigenous Nigerian company '
    'active in midstream and downstream oil and gas, national road haulage and logistics, and '
    'development and operation of port infrastructure.'
)

ABOUT_OPERATIONS = (
    'With this foundation, we offer reliable collection, sorting, and industrial recycling of plastic—'
    'starting in Gombe and Taraba States and designed to scale across Nigeria. Our aim is straightforward: '
    'to keep plastics in circulation as a resource, not as pollution, while creating decent work and '
    'supporting Nigeria’s climate and circular economy goals.'
)

ABOUT_CONTEXT = (
    'Nigeria generates well over a million tonnes of plastic waste every year, with less than 10% '
    'currently recycled. The National Policy on Plastic Waste Management and Extended Producer '
    'Responsibility (EPR) guidelines call for a 5R hierarchy—reduce, repair, reuse, recycle, and recovery. '
    'Nigeria’s Nationally Determined Contributions (NDCs) also promote a more circular, low-carbon waste '
    'sector, including recycling and green jobs. That creates demand for trusted, industrial-scale '
    'recyclers with traceable, policy-aligned services and consistent supply of high-quality recycled polymers.'
)

VISION_TEXT = (
    'To build one of Nigeria’s most efficient, inclusive, and climate-positive plastic recycling '
    'networks—turning plastic waste into wealth while supporting dignified livelihoods for reclaimers '
    'and helping brands meet EPR and climate commitments.'
)

WHY_PARTNER_HEADING_LINE1 = 'Why partner with'
WHY_PARTNER_HEADING_LINE2 = 'Sahel Waste2Wealth?'

WHY_PARTNER_ITEMS = [
    {
        'title': 'Integrated logistics strength',
        'text': (
            'Backed by Sahel Enerlog’s truck fleet and port links, we can scale collection and move '
            'materials efficiently from community to plant to market.'
        ),
    },
    {
        'title': 'Traceable, scalable sourcing',
        'text': (
            'Two sourcing models: industrial stations and community networks creating a diversified '
            'feedstock base and transparent material flows.'
        ),
    },
    {
        'title': 'Socially just by design',
        'text': (
            'Reclaimers, women’s groups and youth cooperatives are treated as partners in the value chain, '
            'with real income opportunities and a route into more formal work as operations grow.'
        ),
    },
    {
        'title': 'Policy-aligned circular partner',
        'text': (
            'Our model is built around Nigeria’s national policies and NDC targets, so your engagement '
            'supports both compliance and climate commitments.'
        ),
    },
    {
        'title': 'Reliable recycled raw materials',
        'text': (
            'The end result is a stable supply of PET and PP recyclate that can be used directly in new '
            'products, reducing costs and environmental impact over time.'
        ),
    },
]

SERVICE_ITEMS = [
    {
        'id': 1,
        'title': 'Collection & aggregation',
        'excerpt': (
            'Individual waste pickers, Cluster Waste2Wealth groups, baling stations, and community '
            'reclaimers—with transparent pricing and Sahel truck pickups.'
        ),
        'image': 'plast4ce/img/service/service_1.jpg',
        'list_icon': 'plast4ce/img/service/bottle.png',
        'thumb': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'hero_image': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'body': (
            'We combine multiple sourcing models: materials supplied to collection and baling stations where '
            'quality is assessed; Cluster Waste2Wealth schemes training and coordinating youth and women’s '
            'groups into neighbourhood clusters; purchasing baled materials from existing centres; and a '
            'community reclaimers network with awareness campaigns, household and school collection points, '
            'regular pickups, basic PPE, and simple, transparent pricing.'
        ),
    },
    {
        'id': 2,
        'title': 'Sorting, washing & flaking',
        'excerpt': (
            'Safe sorting and baling at our stations in Gombe and Jalingo; crushing and washing with a '
            'roadmap to rPET and rPP pellet production.'
        ),
        'image': 'plast4ce/img/service/service_2.jpg',
        'list_icon': 'plast4ce/img/service/bottle.png',
        'thumb': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'hero_image': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'body': (
            'We focus on post-consumer plastics—mainly PET and PP—with processing that improves quality: '
            'less contamination, better flake and pellet specifications. Planned rPET and rPP pellets will '
            'support food-grade and non-food-grade applications tailored to converter specifications.'
        ),
    },
    {
        'id': 3,
        'title': 'Recyclate supply for industry',
        'excerpt': (
            'Sorted bales, washed flakes, or pellets depending on your process and offtake needs—reducing '
            'dependence on imported virgin plastics.'
        ),
        'image': 'plast4ce/img/service/service_3.jpg',
        'list_icon': 'plast4ce/img/service/bottle.png',
        'thumb': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'hero_image': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'body': (
            'Recycled raw materials are supplied to converters and manufacturers for new packaging and '
            'products. Using recycled polymers cuts emissions in your value chain. Backed by SAHEL Enerlog’s '
            'logistics and port access, we can move material efficiently from inland hubs to facilities '
            'across Nigeria or to export points.'
        ),
    },
    {
        'id': 4,
        'title': 'Policy-aligned partnerships',
        'excerpt': (
            'Infrastructure and data producers and PROs can plug into—anchored in national plastic policy, '
            'EPR, and NDC commitments.'
        ),
        'image': 'plast4ce/img/service/service_4.jpg',
        'list_icon': 'plast4ce/img/service/bottle.png',
        'thumb': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'hero_image': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'body': (
            'We provide collection, sorting, and recycling infrastructure aligned with Nigeria’s National '
            'Policy on Plastic Waste Management and the 5R hierarchy; support compliance reporting with data '
            'on volumes collected and recycled; and run awareness and training programmes that help state and '
            'local governments implement plastic action plans. For offtakers and EPR partners, we aim to be a '
            'policy-aligned implementation partner—not only a supplier.'
        ),
    },
]

PROJECT_ITEMS = [
    {
        'id': 1,
        'title': 'Gombe & Jalingo hub operations',
        'image': 'plast4ce/img/project/1.jpg',
        'excerpt': 'Sorting, baling, awareness, and community programmes building source-segregation habits.',
        'body': (
            'Safe sorting and baling at stations in Gombe and Jalingo, with awareness, training, and '
            'community programmes that build practical source-segregation habits in homes and schools—'
            'improving feedstock quality and household income as part of a just transition.'
        ),
    },
    {
        'id': 2,
        'title': 'National scale-up roadmap',
        'image': 'plast4ce/img/project/1.jpg',
        'excerpt': 'Designed to expand beyond Gombe and Taraba with traceable flows and logistics strength.',
        'body': (
            'Our model is built to scale: two sourcing models—industrial stations and community networks—'
            'create a diversified feedstock base and transparent material flows, with integrated logistics '
            'from SAHEL Enerlog’s truck fleet and port links.'
        ),
    },
]

TESTIMONIALS = [
    {
        'quote': (
            'Sahel Plast4CE gives us traceable recovered volumes and stable quality specs, which makes our '
            'EPR and packaging reporting much easier.'
        ),
        'name': 'Amina Yusuf',
        'role': 'Sustainability Manager, FMCG partner',
        'image': 'plast4ce/img/team/abbas.png',
    },
    {
        'quote': (
            'Their team coordinates community collection professionally and keeps pricing transparent, so our '
            'cluster network can plan volumes with confidence.'
        ),
        'name': 'Haruna T. Zango',
        'role': 'Community Cluster Lead',
        'image': 'plast4ce/img/team/haruna.png',
    },
    {
        'quote': (
            'From pickup to processing updates, communication is clear and reliable. That consistency helps '
            'us secure feedstock for recycling operations month after month.'
        ),
        'name': 'Engr. Abubakar Ahmad',
        'role': 'Supply Chain Partner',
        'image': 'plast4ce/img/team/sadiq.png',
    },
    {
        'quote': (
            'The programme creates practical income opportunities for youth while improving waste sorting '
            'discipline in our communities.'
        ),
        'name': 'Ismail I. Abubakar',
        'role': 'Project Delivery Partner',
        'image': 'plast4ce/img/team/ismail.png',
    },
]

TEAM_MEMBERS = [
    {
        'id': 1,
        'name': 'Prof. Shehu U. Hassan',
        'role': 'Founder and Chief Executive',
        'image': 'plast4ce/img/team/prof.png',
        'bio': (
            'Leadership focused on building a resilient, inclusive circular plastics value chain across '
            'Nigeria’s key markets.'
        ),
    },
    {
        'id': 2,
        'name': 'Dr. Abubakar Abubakar',
        'role': 'Chief Financial Officer',
        'image': 'plast4ce/img/team/drabubakar.png',
        'bio': 'Financial stewardship and governance for Plast4CE operations and growth.',
    },
    {
        'id': 3,
        'name': 'Haruna T. Zango',
        'role': 'Chief Commercial Officer',
        'image': 'plast4ce/img/team/haruna.png',
        'bio': 'Commercial strategy and partnerships across the recycling and logistics network.',
    },
    {
        'id': 4,
        'name': 'Ridwan Jaafar',
        'role': 'Partnerships & Sustainability Manager',
        'image': 'plast4ce/img/team/ridwan.png',
        'bio': 'Sustainability programmes and stakeholder alignment with EPR and climate objectives.',
    },
    {
        'id': 5,
        'name': 'Ismail I. Abubakar',
        'role': 'Project Manager',
        'image': 'plast4ce/img/team/ismail.png',
        'bio': 'Delivery of collection, processing, and community programmes on the ground.',
    },
    {
        'id': 6,
        'name': 'Engr. Abubakar Ahmad',
        'role': 'Community & Supply Coordinator',
        'image': 'plast4ce/img/team/sadiq.png',
        'bio': 'Community reclaimers networks, supply quality, and field coordination.',
    },
    {
        'id': 7,
        'name': 'Abbas S. Tafida',
        'role': 'Marketing Manager',
        'image': 'plast4ce/img/team/abbas.png',
        'bio': 'Market development and communications for Plast4CE and partner programmes.',
    },
    {
        'id': 8,
        'name': 'Atiku M. Jafar',
        'role': 'Legal & Compliance',
        'image': 'plast4ce/img/team/atiku.png',
        'bio': 'Legal and compliance support for operations and partnerships.',
    },
]

GALLERY_IMAGES = [
    {
        'src': 'plast4ce/img/project/1.jpg',
        'alt': 'Sorting and baling operations',
        'category': 'Operations',
    },
    {
        'src': 'plast4ce/img/project/2.jpg',
        'alt': 'Collection and aggregation',
        'category': 'Collection',
    },
    {
        'src': 'plast4ce/img/project/3.jpg',
        'alt': 'Material recovery in action',
        'category': 'Processing',
    },
    {
        'src': 'plast4ce/img/project/4.jpg',
        'alt': 'Community engagement',
        'category': 'Community',
    },
    {
        'src': 'plast4ce/img/service/service_1.jpg',
        'alt': 'Plastic recovery service',
        'category': 'Services',
    },
    {
        'src': 'plast4ce/img/service/service_4.jpg',
        'alt': 'Recycling service',
        'category': 'Services',
    },
    {
        'src': 'plast4ce/img/service-details/plastic_recycle.jpg',
        'alt': 'Plastic recycling stream',
        'category': 'Materials',
    },
    {
        'src': 'plast4ce/img/service-details/paper_recycle.jpg',
        'alt': 'Paper recycling stream',
        'category': 'Materials',
    },
]

# Use YouTube watch URL IDs (11 chars). Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ → dQw4w9WgXcQ
GALLERY_VIDEOS = [
    {
        'title': 'Sahel Plast4CE overview',
        'youtube_id': '',
        'thumb': 'plast4ce/img/breadcrumb/service_bg.jpg',
    },
    {
        'title': 'Collection & processing (highlights)',
        'youtube_id': '',
        'thumb': 'plast4ce/img/breadcrumb/project_bg.jpg',
    },
]


def get_by_id(items, pk):
    for item in items:
        if item['id'] == int(pk):
            return item
    return None
