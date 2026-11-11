
from django.contrib import admin
from django.utils.html import format_html

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
    NavigationItem,
    SectionContent,
    PortfolioFilterLabel,
    ContactContent,
    FooterLink,
    BehindScenesImage,
    ContactServiceOption,
    UpcomingProject,
    WhyChooseContent,
    WhyChooseFeature,
)


# --------------------------------------------------
# ADMIN PANEL BRANDING
# --------------------------------------------------

admin.site.site_header = "OG CREATIONS - Admin Panel"
admin.site.site_title = "OG CREATIONS"
admin.site.index_title = "Website Management"


# --------------------------------------------------
# WEBSITE SETTINGS
# --------------------------------------------------

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    list_display = (
        "company_name",
        "email",
        "phone",
        "updated_at",
    )

    readonly_fields = (
        "logo_preview",
        "favicon_preview",
        "updated_at",
    )

    fieldsets = (

        ("Website Branding", {
            "fields": (
                "company_name",
                "tagline",
                "logo",
                "logo_preview",
                "favicon",
                "favicon_preview",
            )
        }),

        ("Contact Information", {
            "fields": (
                "email",
                "phone",
                "address",
            )
        }),

        ("Footer Settings", {
            "fields": (
                "footer_text",
                "copyright_text",
            )
        }),

        ("SEO Settings", {
            "fields": (
                "seo_title",
                "seo_description",
            )
        }),

        ("Record Information", {
            "fields": ("updated_at",)
        }),
    )

    @admin.display(description="Logo Preview")
    def logo_preview(self, obj):

        if obj and obj.logo:
            return format_html(
                '<img src="{}" width="150" '
                'style="object-fit:contain;" />',
                obj.logo.url
            )

        return "No logo uploaded"

    @admin.display(description="Favicon Preview")
    def favicon_preview(self, obj):

        if obj and obj.favicon:
            return format_html(
                '<img src="{}" width="48" height="48" />',
                obj.favicon.url
            )

        return "No favicon uploaded"


# --------------------------------------------------
# HERO BANNER
# --------------------------------------------------

@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):

    list_display = (
        "title_line_one", "title_line_two",
        "is_active", "sort_order"
    )

    list_editable = ("is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("title_line_one", "title_line_two", "eyebrow")

    readonly_fields = ("background_image_preview",)

    fieldsets = (
        ("Hero Content", {
            "fields": (
                "eyebrow", "title_line_one",
                "title_line_two", "description"
            )
        }),
        ("Hero Background", {
            "fields": ("background_image", "background_image_preview")
        }),
        ("Hero Buttons", {
            "fields": (
                "primary_button_text", "primary_button_url",
                "secondary_button_text", "secondary_button_url"
            )
        }),
        ("Production Tags", {
            "fields": ("production_tags",)
        }),
        ("Display Settings", {
            "fields": ("is_active", "sort_order")
        }),
    )

    @admin.display(description="Hero Image Preview")
    def background_image_preview(self, obj):
        if obj and obj.background_image:
            return format_html(
                '<img src="{}" width="300" style="border-radius:8px;" />',
                obj.background_image.url
            )
        return "No image uploaded"


# --------------------------------------------------
# MARQUEE
# --------------------------------------------------

@admin.register(MarqueeItem)
class MarqueeItemAdmin(admin.ModelAdmin):

    list_display = ("label", "is_active", "sort_order")
    list_editable = ("is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("label",)


# --------------------------------------------------
# ABOUT SECTION
# --------------------------------------------------

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):

    list_display = ("eyebrow", "is_active")
    list_editable = ("is_active",)

    readonly_fields = (
        "image_one_preview",
        "image_two_preview",
        "image_three_preview",
    )

    fieldsets = (
        ("About Heading", {
            "fields": (
                "eyebrow", "heading_line_one", "heading_highlight"
            )
        }),
        ("About Description", {
            "fields": ("paragraph_one", "paragraph_two")
        }),
        ("About Images", {
            "fields": (
                "image_one", "image_one_preview",
                "image_two", "image_two_preview",
                "image_three", "image_three_preview",
            )
        }),
        ("About Button", {
            "fields": ("button_text", "button_url")
        }),
        ("Display Settings", {
            "fields": ("is_active",)
        }),
    )

    def _preview(self, image):
        if image:
            return format_html(
                '<img src="{}" width="180" style="border-radius:8px;" />',
                image.url
            )
        return "No image uploaded"

    @admin.display(description="Image One Preview")
    def image_one_preview(self, obj):
        return self._preview(obj.image_one) if obj else "No image uploaded"

    @admin.display(description="Image Two Preview")
    def image_two_preview(self, obj):
        return self._preview(obj.image_two) if obj else "No image uploaded"

    @admin.display(description="Image Three Preview")
    def image_three_preview(self, obj):
        return self._preview(obj.image_three) if obj else "No image uploaded"


# --------------------------------------------------
# SERVICES
# --------------------------------------------------

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title", "number", "is_featured",
        "is_active", "sort_order"
    )

    list_editable = ("number", "is_featured", "is_active", "sort_order")
    list_filter = ("is_active", "is_featured")
    search_fields = ("title", "short_description")
    readonly_fields = ("image_preview",)

    fieldsets = (
        ("Service Content", {
            "fields": ("title", "short_description", "number")
        }),
        ("Service Image", {
            "fields": ("image", "image_preview")
        }),
        ("Display Settings", {
            "fields": ("is_featured", "is_active", "sort_order")
        }),
    )

    @admin.display(description="Service Image Preview")
    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" width="220" style="border-radius:8px;" />',
                obj.image.url
            )
        return "No image uploaded"


# --------------------------------------------------
# PORTFOLIO PROJECTS
# --------------------------------------------------

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title", "category", "client",
        "is_published", "is_featured", "sort_order"
    )

    list_editable = ("is_published", "is_featured", "sort_order")
    list_filter = ("category", "is_published", "is_featured")
    search_fields = ("title", "client", "description")

    readonly_fields = ("cover_image_preview", "created_at")

    fieldsets = (
        ("Project Information", {
            "fields": (
                "title", "category", "client",
                "description", "project_date"
            )
        }),
        ("Project Media", {
            "fields": (
                "cover_image", "cover_image_preview", "video_url"
            )
        }),
        ("Display Settings", {
            "fields": ("is_featured", "is_published", "sort_order")
        }),
        ("Record Information", {
            "fields": ("created_at",)
        }),
    )

    @admin.display(description="Project Image Preview")
    def cover_image_preview(self, obj):
        if obj and obj.cover_image:
            return format_html(
                '<img src="{}" width="240" style="border-radius:8px;" />',
                obj.cover_image.url
            )
        return "No image uploaded"


# --------------------------------------------------
# PRODUCTION PROCESS
# --------------------------------------------------

@admin.register(ProductionStep)
class ProductionStepAdmin(admin.ModelAdmin):

    list_display = ("number", "title", "is_active", "sort_order")
    list_display_links = ("title",)
    list_editable = ("number", "is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("title", "description")


# --------------------------------------------------
# ENQUIRIES
# --------------------------------------------------

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        "name", "email", "phone",
        "service", "status", "created_at"
    )

    list_editable = ("status",)
    list_filter = ("status", "created_at")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = ("created_at",)


# --------------------------------------------------
# SOCIAL LINKS
# --------------------------------------------------

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):

    list_display = (
        "platform",
        "url",
        "is_active",
        "sort_order",
    )

    list_editable = ("is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("platform",)


# --------------------------------------------------
# HEADER NAVIGATION
# --------------------------------------------------

@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):

    list_display = (
        "label", "url", "is_button",
        "open_new_tab", "is_active", "sort_order"
    )

    list_editable = ("is_button", "open_new_tab", "is_active", "sort_order")
    list_filter = ("is_active", "is_button")
    search_fields = ("label", "url")


# --------------------------------------------------
# WEBSITE SECTION CONTENT
# --------------------------------------------------

@admin.register(SectionContent)
class SectionContentAdmin(admin.ModelAdmin):

    list_display = ("section", "eyebrow", "heading", "is_active")
    list_editable = ("is_active",)
    list_filter = ("section", "is_active")
    search_fields = ("eyebrow", "heading", "description")


# --------------------------------------------------
# PORTFOLIO FILTER LABELS
# --------------------------------------------------

@admin.register(PortfolioFilterLabel)
class PortfolioFilterLabelAdmin(admin.ModelAdmin):

    list_display = ("category", "label", "is_active", "sort_order")
    list_editable = ("label", "is_active", "sort_order")
    list_filter = ("is_active",)
    search_fields = ("label",)



@admin.register(ContactContent)
class ContactContentAdmin(admin.ModelAdmin):

    list_display = (
        "eyebrow",
        "heading_line_one",
        "is_active",
    )

    list_editable = ("is_active",)

    list_filter = ("is_active",)

    fieldsets = (

        ("Contact Section Heading", {
            "fields": (
                "eyebrow",
                "heading_line_one",
                "heading_highlight",
                "heading_line_two",
                "is_active",
            )
        }),

        ("Contact Information", {
            "fields": (
                "phone_label",
                "phone",
                "email_label",
                "email",
                "studio_label",
                "studio_address",
            )
        }),

        ("Contact Images and Location", {
            "fields": (
                "background_image",
                "location_image",
                "map_embed_url",
            )
        }),

        ("Enquiry Form Heading", {
            "fields": (
                "form_heading",
            )
        }),

        ("Name Field", {
            "fields": (
                "name_label",
                "name_placeholder",
            )
        }),

        ("Phone Field", {
            "fields": (
                "phone_form_label",
                "phone_placeholder",
            )
        }),

        ("Email Field", {
            "fields": (
                "email_form_label",
                "email_placeholder",
            )
        }),

        ("Service Field", {
            "fields": (
                "service_label",
                "service_placeholder",
            )
        }),

        ("Project Details Field", {
            "fields": (
                "message_label",
                "message_placeholder",
            )
        }),

        ("Submit Button and Messages", {
            "fields": (
                "submit_button_text",
                "success_message",
            )
        }),
    )




# --------------------------------------------------
# FOOTER LINKS
# --------------------------------------------------

@admin.register(FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):

    list_display = (
        "label",
        "section",
        "url",
        "open_new_tab",
        "is_active",
        "sort_order",
    )

    list_editable = (
        "section",
        "open_new_tab",
        "is_active",
        "sort_order",
    )

    list_filter = ("section", "is_active")
    search_fields = ("label", "url")


@admin.register(BehindScenesImage)
class BehindScenesImageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "caption",
        "position",
        "sort_order",
        "is_active",
    )

    list_filter = ("position", "is_active")
    search_fields = ("title", "caption")
    list_editable = ("position", "sort_order", "is_active")
    ordering = ("sort_order", "id")

    readonly_fields = ("image_preview",)

    fields = (
        "title",
        "caption",
        "image",
        "image_preview",
        "position",
        "sort_order",
        "is_active",
    )

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" width="250" style="border-radius:8px;" />',
                obj.image.url
            )
        return "No image uploaded"

    image_preview.short_description = "Image Preview"


@admin.register(ContactServiceOption)
class ContactServiceOptionAdmin(admin.ModelAdmin):

    list_display = (
        "label",
        "value",
        "sort_order",
        "is_active",
    )

    list_editable = (
        "sort_order",
        "is_active",
    )

    list_filter = ("is_active",)

    search_fields = ("label", "value")

    prepopulated_fields = {
        "value": ("label",)
    }

    ordering = ("sort_order", "id")



# -----------------------------------------
# UPCOMING PROJECTS ADMIN
# -----------------------------------------

@admin.register(UpcomingProject)
class UpcomingProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "lead_actor",
        "release_date",
        "is_active",
        "sort_order",
    )

    list_editable = (
        "is_active",
        "sort_order",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "lead_actor",
        "lead_actress",
        "supporting_cast",
    )

    ordering = (
        "sort_order",
        "-created_at",
    )

    fieldsets = (

        ("Project Information", {
            "fields": (
                "project_label",
                "title",
                "tagline",
                "poster",
            )
        }),

        ("Cast Details", {
            "fields": (
                "lead_actor",
                "lead_actress",
                "supporting_cast",
            )
        }),

        ("Release Information", {
            "fields": (
                "release_date",
                "release_note",
            )
        }),

        ("Display Settings", {
            "fields": (
                "is_active",
                "sort_order",
            )
        }),
    )


# -----------------------------------------
# WHY CHOOSE OG CREATIONS
# -----------------------------------------

class WhyChooseFeatureInline(admin.TabularInline):
    model = WhyChooseFeature
    extra = 1
    fields = (
        "number",
        "title",
        "description",
        "is_active",
        "sort_order",
    )
    ordering = ("sort_order", "number")


@admin.register(WhyChooseContent)
class WhyChooseContentAdmin(admin.ModelAdmin):

    list_display = (
        "heading",
        "eyebrow",
        "is_active",
    )

    list_editable = ("is_active",)

    list_filter = ("is_active",)

    search_fields = ("heading", "eyebrow")

    readonly_fields = ("image_preview",)

    fields = (
        "eyebrow",
        "heading",
        "main_image",
        "image_preview",
        "is_active",
    )

    inlines = [WhyChooseFeatureInline]

    @admin.display(description="Main Image Preview")
    def image_preview(self, obj):
        if obj and obj.main_image:
            return format_html(
                '<img src="{}" width="300" '
                'style="border-radius:8px; object-fit:cover;" />',
                obj.main_image.url
            )

        return "No image uploaded"



