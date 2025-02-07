# Mushroom Gallery

A simple static website for showcasing images with accompanying text, built with Jekyll and hosted on GitHub Pages.

## How It Works

1. **Content Folders:**  
   - Place your image files (e.g. `.jpg`, `.png`) in the `images/` folder.  
   - Place your corresponding description files (as `.txt` or `.md`) in the `descriptions/` folder.  
     *Ensure that each description file has the same base name as its image file (e.g., `plant1.jpg` and `plant1.txt`).*

2. **Generate Gallery Pages:**  
   Run the provided script to generate a markdown file for each image in the `_gallery/` folder:
   ```bash
   python3 generate_gallery.py
