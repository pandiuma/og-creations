
from django.db import models


class SiteSettings(models.Model):
    company_name = models.CharField(
        max_length=120,
        default="OG CREATIONS"
    )
    tagline = models.CharField(
        max_length=180,
        default="CONCEPT TO CREATION"
    )
    logo = models.ImageField(
        upload_to="branding/",
        blank=True,
        null=True
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    
    footer_text = models.CharField(
        max_length=255,
        blank=True
    )

    favicon = models.ImageField(
        upload_to="branding/",
        blank=True,
        null=True
    )

    seo_title = models.CharField(
        max_length=180,
        blank=True,
        default="OG CREATIONS | Concept to Creation"
    )

    seo_description = models.TextField(blank=True)

    copyright_text = models.CharField(
        max_length=255,
        blank=True,
        default="© 2026 OG CREATIONS. All rights reserved."
    )

    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = "Website settings"

    def __str__(self):
        return self.company_name


class HeroBanner(models.Model):
    eyebrow = models.CharField(max_length=180, blank=True)

    title_line_one = models.CharField(
        max_length=150,
        default="From Concept"
    )

    title_line_two = models.CharField(
        max_length=150,
        default="to Creation"
    )

    description = models.TextField()

    background_image = models.ImageField(
        upload_to="hero/"
    )

    primary_button_text = models.CharField(
        max_length=60,
        default="Start a Project"
    )

    primary_button_url = models.CharField(
        max_length=255,
        default="#contact"
    )

    secondary_button_text = models.CharField(
        max_length=60,
        default="Explore Our Craft"
    )

    secondary_button_url = models.CharField(
        max_length=255,
        default="#services"
    )

    production_tags = models.CharField(
    max_length=255,
    default="DIRECTION • CINEMATOGRAPHY • ART DIRECTION • POST",
    blank=True
)

    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title_line_one


class MarqueeItem(models.Model):
    label = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.label


class AboutSection(models.Model):
    eyebrow = models.CharField(
        max_length=100,
        default="THE STUDIO"
    )

    heading_line_one = models.CharField(
        max_length=160,
        default="Built for stories that deserve"
    )

    heading_highlight = models.CharField(
        max_length=100,
        default="the big screen."
    )

    paragraph_one = models.TextField()
    paragraph_two = models.TextField(blank=True)

    image_one = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    image_two = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    image_three = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True
    )

    button_text = models.CharField(
        max_length=80,
        default="See What We Produce"
    )

    button_url = models.CharField(
        max_length=255,
        default="#services"
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "About the Studio"


class Service(models.Model):
    title = models.CharField(max_length=120)
    short_description = models.TextField()

    image = models.ImageField(
        upload_to="services/"
    )

    number = models.PositiveIntegerField(default=1)
    is_featured = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "number"]

    def __str__(self):
        return self.title


class PortfolioProject(models.Model):

    CATEGORY_CHOICES = [
        ("movies", "Movies"),
        ("web-series", "Web Series"),
        ("commercials", "Commercials"),
        ("events", "Events"),
        ("music-videos", "Music Videos"),
        ("ad-shoots", "Ad Shoots"),
    ]

    title = models.CharField(max_length=160)

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    client = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)

    cover_image = models.ImageField(
        upload_to="portfolio/"
    )

    project_date = models.DateField(
        blank=True,
        null=True
    )

    video_url = models.URLField(blank=True)

    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "-created_at"]

    def __str__(self):
        return self.title


class ProductionStep(models.Model):
    number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon_text = models.CharField(max_length=12, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "number"]

    def __str__(self):
        return self.title


class Enquiry(models.Model):

    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("in-progress", "In Progress"),
        ("closed", "Closed"),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=120, blank=True)
    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    platform = models.CharField(max_length=60)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]

    def __str__(self):
        return self.platform

# HEADER NAVIGATION

class NavigationItem(models.Model):
    label = models.CharField(max_length=80)
    url = models.CharField(max_length=255)
    is_button = models.BooleanField(default=False)
    open_new_tab = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Navigation item"
        verbose_name_plural = "Header navigation"

    def __str__(self):
        return self.label


# WEBSITE SECTION CONTENT

class SectionContent(models.Model):

    SECTION_CHOICES = [
        ("services", "Services"),
        ("portfolio", "Portfolio"),
        ("process", "Production Process"),
        ("contact", "Contact"),
    ]

    section = models.CharField(
        max_length=30,
        choices=SECTION_CHOICES,
        unique=True
    )

    eyebrow = models.CharField(max_length=150, blank=True)
    heading = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.get_section_display()


# PORTFOLIO FILTER LABELS

class PortfolioFilterLabel(models.Model):

    CATEGORY_CHOICES = [
        ("all", "All Projects"),
        ("movies", "Movies"),
        ("web-series", "Web Series"),
        ("commercials", "Commercials"),
        ("events", "Events"),
        ("music-videos", "Music Videos"),
        ("ad-shoots", "Ad Shoots"),
    ]

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        unique=True
    )

    label = models.CharField(max_length=80)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Portfolio filter"
        verbose_name_plural = "Portfolio filters"

    def __str__(self):
        return self.label



# CONTACT SECTION AND FORM CONTENT

class ContactContent(models.Model):

    # ---------------------------------
    # LEFT SIDE - CONTACT INFORMATION
    # ---------------------------------

    eyebrow = models.CharField(
        max_length=150,
        blank=True,
        default="START A PROJECT"
    )

    heading_line_one = models.CharField(
        max_length=200,
        blank=True,
        default="Have a Story to"
    )

    heading_highlight = models.CharField(
        max_length=100,
        blank=True,
        default="Tell?"
    )

    heading_line_two = models.CharField(
        max_length=200,
        blank=True,
        default="Let's Bring It to Life."
    )

    phone_label = models.CharField(
        max_length=80,
        blank=True,
        default="PHONE"
    )

    phone = models.CharField(
        max_length=30,
        blank=True,
        default="9884277001"
    )

    email_label = models.CharField(
        max_length=80,
        blank=True,
        default="EMAIL"
    )

    email = models.EmailField(
        blank=True,
        default="ogcreationsofficial@gmail.com"
    )

    studio_label = models.CharField(
        max_length=80,
        blank=True,
        default="STUDIO"
    )

    studio_address = models.TextField(
        blank=True,
        default="No. 15, Rajamannar Salai, KK Nagar, Chennai 600 078"
    )

    # ---------------------------------
    # CONTACT IMAGES
    # ---------------------------------

    background_image = models.ImageField(
        upload_to="contact/",
        blank=True,
        null=True,
        help_text="Background image displayed behind the right-side enquiry form."
    )

    location_image = models.ImageField(
        upload_to="contact/",
        blank=True,
        null=True,
        help_text="Location image displayed below contact details on the left."
    )

    map_embed_url = models.URLField(
        blank=True,
        help_text="Optional Google Maps embed URL."
    )

    # ---------------------------------
    # RIGHT SIDE - ENQUIRY FORM
    # ---------------------------------

    form_heading = models.CharField(
        max_length=150,
        blank=True,
        default="START A PROJECT"
    )

    name_label = models.CharField(
        max_length=80,
        blank=True,
        default="FULL NAME *"
    )

    name_placeholder = models.CharField(
        max_length=120,
        blank=True,
        default="Your name"
    )

    phone_form_label = models.CharField(
        max_length=80,
        blank=True,
        default="PHONE NUMBER *"
    )

    phone_placeholder = models.CharField(
        max_length=120,
        blank=True,
        default="+91 98765 43210"
    )

    email_form_label = models.CharField(
        max_length=80,
        blank=True,
        default="EMAIL ADDRESS *"
    )

    email_placeholder = models.CharField(
        max_length=120,
        blank=True,
        default="you@example.com"
    )

    service_label = models.CharField(
        max_length=80,
        blank=True,
        default="SERVICE REQUIRED *"
    )

    service_placeholder = models.CharField(
        max_length=120,
        blank=True,
        default="Select a service"
    )

    message_label = models.CharField(
        max_length=100,
        blank=True,
        default="PROJECT DETAILS *"
    )

    message_placeholder = models.CharField(
        max_length=180,
        blank=True,
        default="Tell us about your project"
    )

    submit_button_text = models.CharField(
        max_length=80,
        blank=True,
        default="START A PROJECT"
    )

    success_message = models.CharField(
        max_length=255,
        blank=True,
        default="Thank you! Your enquiry has been received."
    )

    # ---------------------------------
    # SECTION SETTINGS
    # ---------------------------------

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Contact Section"


# -----------------------------------------
# DYNAMIC CONTACT FORM SERVICE OPTIONS
# -----------------------------------------

class ContactServiceOption(models.Model):

    label = models.CharField(
        max_length=120,
        unique=True
    )

    value = models.SlugField(
        max_length=120,
        unique=True,
        help_text="Value saved when a visitor selects this service."
    )

    sort_order = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Contact Service Option"
        verbose_name_plural = "Contact Service Options"

    def __str__(self):
        return self.label




class BehindScenesImage(models.Model):

    POSITION_CHOICES = [
        ("large", "Large Image"),
        ("small", "Small Image"),
    ]

    title = models.CharField(max_length=120, blank=True)
    caption = models.CharField(max_length=180, blank=True)

    image = models.ImageField(upload_to="behind-scenes/")

    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        default="small"
    )

    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["sort_order", "id"]
        verbose_name = "Behind the Scenes Image"
        verbose_name_plural = "Behind the Scenes Gallery"

    def __str__(self):
        return self.title or self.caption or f"Behind the Scenes {self.pk}"



# FOOTER LINKS

class FooterLink(models.Model):

    SECTION_CHOICES = [
        ("navigate", "Navigate"),
        ("services", "Services"),
    ]

    section = models.CharField(
        max_length=20,
        choices=SECTION_CHOICES,
        default="navigate"
    )

    label = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)

    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)
    open_new_tab = models.BooleanField(default=False)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.label


# -----------------------------------------
# UPCOMING PROJECTS
# -----------------------------------------

class UpcomingProject(models.Model):

    project_label = models.CharField(
        max_length=80,
        default="UPCOMING"
    )

    title = models.CharField(
        max_length=180
    )

    tagline = models.TextField(
        blank=True
    )

    lead_actor = models.CharField(
        max_length=150,
        blank=True
    )

    lead_actress = models.CharField(
        max_length=150,
        blank=True
    )

    supporting_cast = models.TextField(
        blank=True,
        help_text="Enter supporting cast names."
    )

    release_date = models.CharField(
        max_length=80,
        blank=True,
        help_text="Example: DEC 2026"
    )

    release_note = models.CharField(
        max_length=100,
        default="IN CINEMAS"
    )

    poster = models.ImageField(
        upload_to="upcoming-projects/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True
    )

    sort_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["sort_order", "-created_at"]
        verbose_name = "Upcoming Project"
        verbose_name_plural = "Upcoming Projects"

    def __str__(self):
        return self.title



# -----------------------------------------
# WHY CHOOSE OG CREATIONS
# -----------------------------------------

class WhyChooseContent(models.Model):

    eyebrow = models.CharField(
        max_length=150,
        default="WHY CHOOSE OG CREATIONS"
    )

    heading = models.CharField(
        max_length=200,
        default="Crafted with Intent"
    )

    main_image = models.ImageField(
        upload_to="why-choose/",
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.heading


class WhyChooseFeature(models.Model):

    content = models.ForeignKey(
        WhyChooseContent,
        on_delete=models.CASCADE,
        related_name="features"
    )

    number = models.PositiveIntegerField(default=1)

    title = models.CharField(max_length=150)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "number"]
        verbose_name = "Why Choose Feature"
        verbose_name_plural = "Why Choose Features"

    def __str__(self):
        return self.title


