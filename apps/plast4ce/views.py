from django.http import Http404
from django.shortcuts import render
from apps.plast4ce.demo_content import (
    BLOG_POSTS,
    PROJECT_ITEMS,
    SERVICE_ITEMS,
    SHOP_PRODUCTS,
    SITE_NAME,
    TAGLINE,
    TEAM_MEMBERS,
    get_by_id,
)


def _base_context(**extra):
    ctx = {
        'site_name': SITE_NAME,
        'division_tagline': TAGLINE,
    }
    ctx.update(extra)
    return ctx


def home(request):
    context = _base_context(
        nav_section='home',
        meta_description=(
            'Sahel Plast4ce — recycling, recovery, and sustainability programs with transparent operations '
            'and measurable diversion.'
        ),
        stats=[
            {
                'icon_class': 'las la-recycle',
                'count': 120,
                'heading': 'Tons',
                'sub': 'diverted monthly (demo metric)',
            },
        ],
        services=SERVICE_ITEMS,
        projects=PROJECT_ITEMS,
        posts=BLOG_POSTS,
        team_members=TEAM_MEMBERS,
        testimonials=[
            {
                'quote': (
                    'Sahel Plast4ce gave us clear reporting and cleaner streams—we finally trust the numbers.'
                ),
                'name': 'Operations director',
                'role': 'Industrial campus',
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
        meta_description='Learn how Sahel Plast4ce advances recycling, recovery, and sustainability outcomes across the region.',
    )
    return render(request, 'plast4ce/about.html', context)


def contact(request):
    context = _base_context(
        nav_section='contact',
        page_heading='Contact',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Contact')],
        meta_description='Reach Sahel Plast4ce for collection, processing, and circularity partnerships.',
    )
    return render(request, 'plast4ce/contact.html', context)


def faq(request):
    context = _base_context(
        nav_section='faq',
        page_heading='FAQ',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'FAQ')],
        meta_description='Answers to common questions about Sahel Plast4ce services and coverage.',
        faq_items=[
            {
                'q': 'What regions do you cover?',
                'a': 'We plan and execute corridor projects across the Sahel and neighboring trade routes.',
            },
        ],
    )
    return render(request, 'plast4ce/faq.html', context)


def pricing(request):
    context = _base_context(
        nav_section='pricing',
        page_heading='Pricing',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Pricing')],
        meta_description='Engagement options for recycling, recovery, and sustainability programs with Sahel Plast4ce.',
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
        meta_description='Material recovery and recycling services from Sahel Plast4ce.',
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
        meta_description='Highlighted programs delivered by Sahel Plast4ce.',
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
        meta_description='Meet the Sahel Plast4ce leadership and delivery team.',
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


def shop(request):
    context = _base_context(
        nav_section='shop',
        page_heading='Shop',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Shop')],
        meta_description='Industrial supplies and kits curated by Sahel Plast4ce.',
        products=SHOP_PRODUCTS,
    )
    return render(request, 'plast4ce/shop.html', context)


def shop_detail(request, pk):
    item = get_by_id(SHOP_PRODUCTS, pk)
    if not item:
        raise Http404('Product not found')
    context = _base_context(
        nav_section='shop',
        product=item,
        page_heading=item['title'],
        breadcrumbs=[
            ('plast4ce:plast4ce_home', 'Home'),
            ('plast4ce:plast4ce_shop', 'Shop'),
            (None, item['title']),
        ],
        meta_description=item['excerpt'],
    )
    return render(request, 'plast4ce/shop_detail.html', context)


def cart(request):
    context = _base_context(
        nav_section='shop',
        page_heading='Cart',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Cart')],
        meta_description='Review items before checkout with Sahel Plast4ce.',
        cart_lines=SHOP_PRODUCTS[:1],
    )
    return render(request, 'plast4ce/cart.html', context)


def checkout(request):
    context = _base_context(
        nav_section='shop',
        page_heading='Checkout',
        breadcrumbs=[('plast4ce:plast4ce_home', 'Home'), (None, 'Checkout')],
        meta_description='Secure checkout flow for Sahel Plast4ce storefront demos.',
        cart_lines=SHOP_PRODUCTS[:1],
    )
    return render(request, 'plast4ce/checkout.html', context)


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
