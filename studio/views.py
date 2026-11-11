

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect

from .models import (
    SiteSettings,
    HeroBanner,
    MarqueeItem,
    AboutSection,
    Service,
    PortfolioProject,
    ProductionStep,
    Enquiry,
    SocialLink,
    BehindScenesImage,
    ContactContent,
    ContactServiceOption,
    FooterLink,
    UpcomingProject,
    WhyChooseContent,
    WhyChooseFeature,
)

from .forms import EnquiryForm


# -----------------------------------------
# HOME PAGE
# -----------------------------------------

def home(request):

    context = {
        "site": SiteSettings.objects.first(),

        "hero": HeroBanner.objects.filter(
            is_active=True
        ).first(),

        "marquee_items": MarqueeItem.objects.filter(
            is_active=True
        ).order_by("sort_order", "id"),

        "about": AboutSection.objects.filter(
            is_active=True
        ).first(),

        "services": Service.objects.filter(
            is_active=True
        ),

        "projects": PortfolioProject.objects.filter(
            is_published=True
        ).order_by("sort_order", "-created_at"),

        "steps": ProductionStep.objects.filter(
            is_active=True
        ),

        "social_links": SocialLink.objects.filter(
            is_active=True
        ),

        # FOOTER LINKS
        "footer_navigation": FooterLink.objects.filter(
            section="navigate",
            is_active=True
        ),

        "footer_services": FooterLink.objects.filter(
            section="services",
            is_active=True
        ),

        # BEHIND THE SCENES
        "behind_scenes_images": BehindScenesImage.objects.filter(
            is_active=True
        ).exclude(
            image=""
        ).order_by("sort_order", "id")[:5],

        # CONTACT SECTION
        "contact": ContactContent.objects.filter(
            is_active=True
        ).first(),

        # CONTACT FORM SERVICE OPTIONS
        "contact_service_options": ContactServiceOption.objects.filter(
            is_active=True
        ),

        # UPCOMING PROJECTS
        "upcoming_projects": UpcomingProject.objects.filter(
            is_active=True
        ).exclude(
            title=""
        ).order_by("sort_order", "-created_at"),

        # WHY CHOOSE OG CREATIONS
        "why_choose": WhyChooseContent.objects.filter(
            is_active=True
        ).first(),

        "why_choose_features": WhyChooseFeature.objects.filter(
            content__is_active=True,
            is_active=True
        ).select_related(
            "content"
        ).order_by("sort_order", "number"),

        # ENQUIRY FORM
        "form": EnquiryForm(),
    }

    return render(
        request,
        "studio/home.html",
        context
    )


# -----------------------------------------
# SUBMIT ENQUIRY
# -----------------------------------------

def submit_enquiry(request):

    if request.method == "POST":

        form = EnquiryForm(request.POST)

        if form.is_valid():

            form.save()

            contact = ContactContent.objects.filter(
                is_active=True
            ).first()

            success_text = (
                contact.success_message
                if contact and contact.success_message
                else "Thank you! Your enquiry has been received."
            )

            messages.success(
                request,
                success_text
            )

        else:

            messages.error(
                request,
                "Please enter valid details."
            )

    return redirect("/#contact")


# -----------------------------------------
# ADMIN DASHBOARD
# -----------------------------------------

@staff_member_required
def dashboard(request):

    context = {

        "enquiry_count": Enquiry.objects.count(),

        "new_enquiry_count": Enquiry.objects.filter(
            status="new"
        ).count(),

        "service_count": Service.objects.count(),

        "project_count": PortfolioProject.objects.count(),

        "recent_enquiries": Enquiry.objects.all()[:8],

    }

    return render(
        request,
        "studio/dashboard.html",
        context
    )

