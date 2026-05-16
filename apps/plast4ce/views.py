from django.http import Http404
from django.shortcuts import render
from django.templatetags.static import static
from apps.plast4ce.demo_content import (
    ABOUT_CONTEXT,
    ABOUT_INTRO,
    ABOUT_OPERATIONS,
    WHY_PARTNER_HEADING_LINE1,
    WHY_PARTNER_HEADING_LINE2,
    WHY_PARTNER_ITEMS,
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
    TESTIMONIALS,
    TEAM_MEMBERS,
    VISION_TEXT,
    get_by_id,
)
from apps.plast4ce.models import GalleryImage, Project


def _project_image_url(item):
    image = item.image
    return image.url if image else ''


def _gallery_image_url(item):
    image = item.image
    return image.url if image else ''


def _project_to_dict(item):
    return {
        'id': item.id,
        'title': item.title,
        'excerpt': item.excerpt,
        'body': item.body,
        'image_url': _project_image_url(item),
    }


def _project_demo_to_dict(item):
    return {
        'id': item['id'],
        'title': item['title'],
        'excerpt': item['excerpt'],
        'body': item.get('body', ''),
        'image': item['image'],
        'image_url': static(item['image']),
    }


def _gallery_demo_to_dict(item):
    return {
        'category': item['category'],
        'alt': item['alt'],
        'src': item['src'],
        'image_url': static(item['src']),
    }


def _get_projects_data():
    project_qs = Project.objects.filter(is_published=True)
    if project_qs.exists():
        return [_project_to_dict(item) for item in project_qs]
    return [_project_demo_to_dict(item) for item in PROJECT_ITEMS]


def _get_gallery_images_data():
    image_qs = GalleryImage.objects.filter(is_published=True)
    if image_qs.exists():
        return [
            {
                'category': item.category or 'Gallery',
                'alt': item.alt_text or item.category or 'Gallery image',
                'image_url': _gallery_image_url(item),
            }
            for item in image_qs
        ]
    return [_gallery_demo_to_dict(item) for item in GALLERY_IMAGES]


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
    projects_data = _get_projects_data()
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
        projects=projects_data,
        team_members=TEAM_MEMBERS,
        testimonials=TESTIMONIALS,
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
    projects_data = _get_projects_data()
    context = _base_context(
        nav_section='projects',
        page_heading='Projects',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Projects')],
        meta_description=f'Highlighted programs delivered by {SITE_NAME}.',
        projects=projects_data,
    )
    return render(request, 'plast4ce/projects.html', context)


def project_detail(request, pk):
    project = Project.objects.filter(pk=pk, is_published=True).first()
    if project:
        item = _project_to_dict(project)
    else:
        item = get_by_id(PROJECT_ITEMS, pk)
        if item:
            item = _project_demo_to_dict(item)
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
    gallery_images_data = _get_gallery_images_data()
    context = _base_context(
        nav_section='gallery',
        page_heading='Gallery',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Gallery')],
        meta_description=f'Photo and video gallery from {SITE_NAME}.',
        gallery_images=gallery_images_data,
        gallery_videos=GALLERY_VIDEOS,
    )
    return render(request, 'plast4ce/gallery.html', context)


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
