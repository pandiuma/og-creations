from pathlib import Path
from django.conf import settings
from django.db.models import ImageField
import cloudinary.uploader

from studio.models import (
    SiteSettings, HeroBanner, AboutSection, Service,
    PortfolioProject, ContactContent, BehindScenesImage,
    UpcomingProject, WhyChooseContent
)

models = [
    SiteSettings, HeroBanner, AboutSection, Service,
    PortfolioProject, ContactContent, BehindScenesImage,
    UpcomingProject, WhyChooseContent
]

files = set()

for model in models:
    for field in model._meta.fields:
        if isinstance(field, ImageField):
            for name in model.objects.values_list(field.name, flat=True):
                if name:
                    files.add(str(name).replace("\\", "/"))

uploaded = 0
failed = 0

for name in sorted(files):
    local_path = Path(settings.MEDIA_ROOT) / name
    public_id = "og_creations_media/" + Path(name).with_suffix("").as_posix()

    try:
        result = cloudinary.uploader.upload(
            str(local_path),
            public_id=public_id,
            resource_type="image",
            overwrite=True,
            unique_filename=False,
            use_filename=False,
            tags=["og_creations_media"]
        )
        print("[UPLOADED]", name, "->", result["public_id"])
        uploaded += 1

    except Exception as e:
        print("[FAILED]", name, "|", str(e))
        failed += 1

print("\n========== UPLOAD SUMMARY ==========")
print("Total images:", len(files))
print("Successfully uploaded:", uploaded)
print("Failed:", failed)
