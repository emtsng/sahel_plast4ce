from django.http import Http404
from django.shortcuts import render
from apps.plast4ce.demo_content import (
    ABOUT_CONTEXT,
    ABOUT_INTRO,
    ABOUT_OPERATIONS,
    WHY_PARTNER_HEADING_LINE1,
    WHY_PARTNER_HEADING_LINE2,
    WHY_PARTNER_ITEMS,
    BLOG_POSTS,
    COMPANY_PROFILE_PDF,
    COMPANY_WEBSITE_LABEL,
    COMPANY_WEBSITE_URL,
    CONTACT_ADDRESS,
    CONTACT_PHONE_DISPLAY,
    CONTACT_PHONE_TEL,
    HERO_SLIDES,
    HOME_ABOUT_BODY,
    HOME_ABOUT_HIGHLIGHT,
    HOME_ABOUT_LABEL,
    HOME_ABOUT_TITLE,
    HOME_ABOUT_YOUTUBE_VIDEO_ID,
    PARENT_COMPANY,
    PROJECT_ITEMS,
    SERVICE_ITEMS,
    GALLERY_IMAGES,
    GALLERY_VIDEOS,
    SITE_NAME,
    TAGLINE,
    TEAM_MEMBERS,
    VISION_TEXT,
    get_by_id,
)


def _base_context(**extra):
    ctx = {
        'site_name': SITE_NAME,
        'division_tagline': TAGLINE,
        'parent_company': PARENT_COMPANY,
        'contact_phone': CONTACT_PHONE_DISPLAY,
        'contact_phone_tel': CONTACT_PHONE_TEL,
        'contact_address': CONTACT_ADDRESS,
        'company_website_url': COMPANY_WEBSITE_URL,
        'company_website_label': COMPANY_WEBSITE_LABEL,
        'company_profile_pdf': COMPANY_PROFILE_PDF,
    }
    ctx.update(extra)
    return ctx


def home(request):
    context = _base_context(
        nav_section='home',
        meta_description=(
            f'{SITE_NAME} — plastic collection, sorting, washing, and recyclate supply for PET and PP, '
            'aligned with Nigeria’s plastic policy and EPR. Operations in Gombe and Taraba.'
        ),
        hero_slides=HERO_SLIDES,
        home_about_label=HOME_ABOUT_LABEL,
        home_about_title=HOME_ABOUT_TITLE,
        home_about_highlight=HOME_ABOUT_HIGHLIGHT,
        home_about_body=HOME_ABOUT_BODY,
        home_about_youtube_video_id=HOME_ABOUT_YOUTUBE_VIDEO_ID,
        stats=[
            {
                'icon_class': 'las la-users',
                'count': 20,
                'heading': 'Staff',
                'sub': '60% women across facilities',
            },
            {
                'icon_class': 'las la-map-marked-alt',
                'count': 2,
                'heading': 'States',
                'sub': 'Gombe & Taraba hub operations',
            },
            {
                'icon_class': 'las la-industry',
                'count': 10,
                'heading': 'Percent',
                'sub': 'national plastic recycling rate context (under 10%)',
            },
        ],
        services=SERVICE_ITEMS,
        projects=PROJECT_ITEMS,
        posts=BLOG_POSTS,
        team_members=TEAM_MEMBERS,
        testimonials=[
            {
                'quote': (
                    'Sahel Plast4CE gives us traceable volumes and community-linked sourcing—aligned with '
                    'our EPR reporting needs.'
                ),
                'name': 'Sustainability lead',
                'role': 'Brand & packaging partner',
                'image': 'plast4ce/img/testimonial/1.jpg',
            },
        ],
    )
    return render(request, 'plast4ce/index.html', context)


def about(request):
    context = _base_context(
        nav_section='about',
        page_heading='About us',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'About')],
        meta_description=(
            f'About {SITE_NAME}: circular plastics unit of {PARENT_COMPANY}, operating in Gombe and Taraba '
            'with collection through washing and flaking for PET and PP.'
        ),
        about_intro=ABOUT_INTRO,
        about_operations=ABOUT_OPERATIONS,
        about_context=ABOUT_CONTEXT,
        vision_text=VISION_TEXT,
        why_partner_heading_line1=WHY_PARTNER_HEADING_LINE1,
        why_partner_heading_line2=WHY_PARTNER_HEADING_LINE2,
        why_partner_items=WHY_PARTNER_ITEMS,
    )
    return render(request, 'plast4ce/about.html', context)


def contact(request):
    context = _base_context(
        nav_section='contact',
        page_heading='Contact',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Contact')],
        meta_description=(
            f'Contact {SITE_NAME} at {CONTACT_ADDRESS}. Phone {CONTACT_PHONE_DISPLAY}. '
            f'Parent group: {COMPANY_WEBSITE_LABEL}.'
        ),
    )
    return render(request, 'plast4ce/contact.html', context)


def faq(request):
    context = _base_context(
        nav_section='faq',
        page_heading='FAQ',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'FAQ')],
        meta_description=f'FAQ about {SITE_NAME}: materials, locations, EPR alignment, and partnerships.',
        faq_items=[
            {
                'q': 'Where does Sahel Plast4CE operate?',
                'a': (
                    'Collection, sorting, and processing are active in Gombe and Taraba States, with a roadmap '
                    'to scale across Nigeria—supported by SAHEL Enerlog’s logistics and port links.'
                ),
            },
            {
                'q': 'Which plastics do you focus on?',
                'a': (
                    'Post-consumer plastics—mainly PET and PP—with sorted bales, washed flakes, and a roadmap to '
                    'rPET and rPP pellets for converters.'
                ),
            },
            {
                'q': 'How do you align with national policy?',
                'a': (
                    'Our programme is anchored in Nigeria’s National Policy on Plastic Waste Management, the 5R '
                    'hierarchy, EPR guidelines, and NDC commitments on waste and circular economy.'
                ),
            },
            {
                'q': 'How do reclaimers and communities participate?',
                'a': (
                    'Through Cluster Waste2Wealth schemes, community collection points, transparent pricing, basic '
                    'PPE, and integration of reclaimers, women’s groups, and youth cooperatives as partners in the '
                    'value chain.'
                ),
            },
        ],
    )
    return render(request, 'plast4ce/faq.html', context)


def pricing(request):
    context = _base_context(
        nav_section='pricing',
        page_heading='Pricing',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Pricing')],
        meta_description=f'Engagement options for recycling, recovery, and sustainability programs with {SITE_NAME}.',
        plans=[
            {
                'name': 'Collection pilot',
                'amount': '249',
                'period': 'per month (demo)',
                'features': [
                    'Route design workshop',
                    'Monthly diversion report',
                    'Processor introductions',
                ],
            },
        ],
    )
    return render(request, 'plast4ce/pricing.html', context)


def services(request):
    context = _base_context(
        nav_section='services',
        page_heading='Services',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Services')],
        meta_description=f'Material recovery and recycling services from {SITE_NAME}.',
        services=SERVICE_ITEMS,
    )
    return render(request, 'plast4ce/services.html', context)


def service_detail(request, pk):
    item = get_by_id(SERVICE_ITEMS, pk)
    if not item:
        raise Http404('Service not found')
    context = _base_context(
        nav_section='services',
        service=item,
        page_heading=item['title'],
        breadcrumbs=[
            ('plast4ce:plast4ce_home', 'Home'),
            ('plast4ce:plast4ce_services', 'Services'),
            (None, item['title']),
        ],
        meta_description=item['excerpt'],
    )
    return render(request, 'plast4ce/service_detail.html', context)


def projects(request):
    context = _base_context(
        nav_section='projects',
        page_heading='Projects',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Projects')],
        meta_description=f'Highlighted programs delivered by {SITE_NAME}.',
        projects=PROJECT_ITEMS,
    )
    return render(request, 'plast4ce/projects.html', context)


def project_detail(request, pk):
    item = get_by_id(PROJECT_ITEMS, pk)
    if not item:
        raise Http404('Project not found')
    context = _base_context(
        nav_section='projects',
        project=item,
        page_heading=item['title'],
        breadcrumbs=[
            ('plast4ce:plast4ce_home', 'Home'),
            ('plast4ce:plast4ce_projects', 'Projects'),
            (None, item['title']),
        ],
        meta_description=item['excerpt'],
    )
    return render(request, 'plast4ce/project_detail.html', context)

def gallery(request):
    context = _base_context(
        nav_section='gallery',
        page_heading='Gallery',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Gallery')],
        meta_description=f'Photo and video gallery from {SITE_NAME}.',
        gallery_images=GALLERY_IMAGES,
        gallery_videos=GALLERY_VIDEOS,
    )
    return render(request, 'plast4ce/gallery.html', context)


def blog(request):
    context = _base_context(
        nav_section='blog',
        page_heading='Blog',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Blog')],
        meta_description='Insights on recycling markets, traceability, and sustainable operations.',
        posts=BLOG_POSTS,
    )
    return render(request, 'plast4ce/blog.html', context)


def blog_detail(request, pk):
    item = get_by_id(BLOG_POSTS, pk)
    if not item:
        raise Http404('Article not found')
    context = _base_context(
        nav_section='blog',
        post=item,
        page_heading=item['title'],
        breadcrumbs=[
            ('plast4ce:plast4ce_home', 'Home'),
            ('plast4ce:plast4ce_blog', 'Blog'),
            (None, item['title']),
        ],
        meta_description=item['excerpt'],
    )
    return render(request, 'plast4ce/blog_detail.html', context)


def team(request):
    context = _base_context(
        nav_section='team',
        page_heading='Team',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Team')],
        meta_description=f'Meet the {SITE_NAME} leadership and delivery team.',
        team_members=TEAM_MEMBERS,
    )
    return render(request, 'plast4ce/team.html', context)


def team_detail(request, pk):
    item = get_by_id(TEAM_MEMBERS, pk)
    if not item:
        raise Http404('Team member not found')
    context = _base_context(
        nav_section='team',
        member=item,
        page_heading=item['name'],
        breadcrumbs=[
            ('plast4ce:plast4ce_home', 'Home'),
            ('plast4ce:plast4ce_team', 'Team'),
            (None, item['name']),
        ],
        meta_description=item['role'],
    )
    return render(request, 'plast4ce/team_detail.html', context)


def handler404(request, exception):
    return render(
        request,
        '404.html',
        _base_context(
            nav_section='',
            meta_description='Page not found.',
        ),
        status=404,
    )
