import os
import re
import subprocess
from PIL import Image

subprocess.run(["git", "clone", "https://github.com/surisuririsu/gakumas-data"])

IMAGE_SIZES = {
    "idols": 24,
    "pIdols": 96,
    "pItems/details": 500,
    "pItems/icons": 96,
    "skillCards/details": 500,
    "skillCards/icons": 96,
}

for image_type, size in IMAGE_SIZES.items():
    directory = f"gakumas-data/images/{image_type}"
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and f.endswith(".png"):
            im = Image.open(f)
            width, height = im.size
            im = im.resize((size, int(height * size / width)))
            im.save(
                f"public/{re.sub('([A-Z]+)', r'_\1',image_type).lower()}/{filename}"
            )

subprocess.run(["rm", "-rf", "gakumas-data"])