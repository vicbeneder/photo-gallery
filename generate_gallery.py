#!/usr/bin/env python3
"""
generate_gallery.py

Scans the `images/` folder for image files and creates corresponding markdown files in `_gallery/`
by reading matching text files from the `descriptions/` folder.
"""

import os

# Directories
IMAGES_DIR = "images"
DESCRIPTIONS_DIR = "descriptions"
OUTPUT_DIR = "_gallery"

# Create output directory if it does not exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Allowed image extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif"]

# Process each file in the images directory
for image_file in os.listdir(IMAGES_DIR):
    base, ext = os.path.splitext(image_file)
    if ext.lower() in image_extensions:
        # Relative image path for the generated markdown file
        image_path = f"/{IMAGES_DIR}/{image_file}"

        # Look for a matching description file (.txt or .md)
        description_file = None
        for possible_ext in [".txt", ".md"]:
            candidate = base + possible_ext
            candidate_path = os.path.join(DESCRIPTIONS_DIR, candidate)
            if os.path.exists(candidate_path):
                description_file = candidate_path
                break

        if description_file:
            with open(description_file, "r", encoding="utf-8") as f:
                description_content = f.read().strip()
        else:
            description_content = "No description available."

        # Precompute the fixed description string
        fixed_description = description_content.replace("\n", "\n  ")

        # Prepare the markdown content with YAML front matter.
        markdown_content = f"""---
title: "{base}"
image: "{image_path}"
description: |
  {fixed_description}
layout: gallery_item
---"""
        # Write to a file in the _gallery directory
        output_file = os.path.join(OUTPUT_DIR, f"{base}.md")
        with open(output_file, "w", encoding="utf-8") as out_f:
            out_f.write(markdown_content)
        print(f"Generated {output_file}")
