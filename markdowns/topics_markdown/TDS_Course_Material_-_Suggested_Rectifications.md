# TDS Course Material - Suggested Rectifications
_Slug: _

---
**Post ID:** 628059  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-course-material-suggested-rectifications/175427/1  

The Python code given in the “Images: Compression” section needs rectification. On reviewing the code below, I saw the following issues:



Not using await inside an async function.
compress_image(…) is marked ‘async’, even though it doesn’t really do anything asynchronous. If I am not mistaken, PIL operations (like img.convert(…)) are synchronous and blocking.

`from pathlib import Path
from PIL import Image
import io

async def compress_image(input_path: Path, output_path: Path, quality: int = 85) -> None:
    """Compress an image while maintaining reasonable quality."""
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        # Optimize for web
        img.save(output_path, 'WEBP', quality=quality, optimize=True)

# Batch process images
paths = Path('images').glob('*.jpg')
for p in paths:
    await compress_image(p, p.with_suffix('.webp'))`
Removing async and await worked fine for me.


Note to Moderators: Kindly keep this active or (in case there is already a similar post) merge it with a related post.

---
**Post ID:** 628257  
**URL:** https://discourse.onlinedegree.iitm.ac.in/t/tds-course-material-suggested-rectifications/175427/2  

[![The image shows a brief description of GitHub Pages, a free static hosting service provided by GitHub.  It automatically publishes the content of a GitHub repository as a website whenever changes are pushed.  The description highlights its usefulness for sharing various types of content, such as analysis results, portfolios, and documentation.
](https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/7/e/7eea833745c4d394dcb9ab7409bd909a8dcde673_2_345x71.png)image1032×213 10.1 KB](https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/7/e/7eea833745c4d394dcb9ab7409bd909a8dcde673.png)


I think the term “static website” is missing in the definition. It should be: “[GitHub Pages](https://pages.github.com/) is a free hosting service that turns your GitHub repository directly into a static website whenever you push it.”

