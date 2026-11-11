
from django.core.management.base import BaseCommand

from studio.models import (
    SiteSettings,
    MarqueeItem,
    Service,
    ProductionStep,
)


class Command(BaseCommand):

    help = "Create initial OG Creations website content"

    def handle(self, *args, **options):

        SiteSettings.objects.get_or_create(
            pk=1,
            defaults={
                "company_name": "OG CREATIONS",
                "tagline": "CONCEPT TO CREATION",
                "email": "hello@ogcreations.in",
                "phone": "+91 00000 00000",
                "footer_text": "Stories made with cinematic care.",
            }
        )

        marquee_items = [
            "MODELLING",
            "EVENTS",
            "MOVIES",
            "WEB SERIES",
            "CASTING",
            "AD SHOOTS",
            "MUSIC VIDEOS",
        ]

        for index, label in enumerate(marquee_items, 1):

            MarqueeItem.objects.get_or_create(
                label=label,
                defaults={"sort_order": index}
            )

        services = [
            (
                "Film & Movie Production",
                "Creative movie production from concept to final frame.",
                1,
            ),
            (
                "Commercials & Ad Films",
                "Cinematic advertising and brand storytelling.",
                2,
            ),
            (
                "Casting & Modelling",
                "Professional talent selection and modelling.",
                3,
            ),
            (
                "Events & Live Production",
                "Creative event planning and production.",
                4,
            ),
            (
                "Web Series",
                "Episodic content for digital platforms.",
                5,
            ),
            (
                "Post Production",
                "Editing, colour grading and sound finishing.",
                6,
            ),
        ]

        for title, description, number in services:

            self.stdout.write(
                f"Add service: {title}"
            )

            Service.objects.get_or_create(
                title=title,
                defaults={
                    "short_description": description,
                    "number": number,
                    "image": "services/placeholder.jpg",
                }
            )

        steps = [
            (
                "Discover",
                "Understand the client's creative vision.",
            ),
            (
                "Develop",
                "Create concepts, scripts and production plans.",
            ),
            (
                "Produce",
                "Bring the story to life with our production team.",
            ),
            (
                "Deliver",
                "Complete editing and final delivery.",
            ),
        ]

        for number, (title, description) in enumerate(steps, 1):

            ProductionStep.objects.get_or_create(
                number=number,
                defaults={
                    "title": title,
                    "description": description,
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "OG CREATIONS starter content created successfully."
            )
        )
