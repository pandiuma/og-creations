from django.conf import settings
from django.db.models import ImageField
from django.core.files.storage import storages
from studio.models import (
    SiteSettings, HeroBanner, AboutSection, Service,
    PortfolioProject, ContactContent, BehindScenesImage,
    UpcomingProject, WhyChooseContent
)
import requests

models = [
    SiteSettings, HeroBanner, AboutSection, Service,
    PortfolioProject, ContactContent, BehindScenesImage,
    UpcomingProject, WhyChooseContent
]

storage = storages["default"]
files = set()

for model in models:
    for field in model._meta.fields:
        if isinstance(field, ImageField):
            for name in model.objects.values_list(field.name, flat=True):
                if name:
                    files.add(str(name).replace("\\", "/"))

success = 0
failed = 0

for name in sorted(files):
    try:
        url = storage.url(name)
        response = requests.get(url, timeout=30)

        if response.status_code == 200 and response.headers.get("Content-Type", "").startswith("image/"):
            print("[OK]", name)
            success += 1
        else:
            print("[FAILED]", name, response.status_code, response.headers.get("Content-Type"))
            failed += 1

    except Exception as e:
        print("[ERROR]", name, str(e))
        failed += 1

print("\n========== VERIFICATION SUMMARY ==========")
print("Total images:", len(files))
print("Working images:", success)
print("Failed images:", failed)
