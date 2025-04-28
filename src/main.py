import sys
import os
from markdown_to_htmlnode import markdown_to_html
from extractmarkdown import extract_title

def copydir(src_dir="static", dest_dir="public"):
    """
    Recursively copies all contents from src_dir to dest_dir.
    First deletes all contents of dest_dir to ensure a clean copy.
    """
    import shutil
    import logging
    
    # Set up logging
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    
    # Delete destination directory if it exists
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        logging.info(f"Deleted existing {dest_dir} directory")
    
    # Create destination directory
    os.makedirs(dest_dir)
    logging.info(f"Created new {dest_dir} directory")
    
    def copy_recursive(src, dest):
        """Helper function to recursively copy files and directories"""
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dest_path = os.path.join(dest, item)
            
            if os.path.isdir(src_path):
                # If it's a directory, create it and recurse
                os.makedirs(dest_path)
                logging.info(f"Created directory: {dest_path}")
                copy_recursive(src_path, dest_path)
            else:
                # If it's a file, copy it
                shutil.copy2(src_path, dest_path)
                logging.info(f"Copied file: {dest_path}")
    
    # Start the recursive copy
    copy_recursive(src_dir, dest_dir)
    logging.info(f"Successfully copied all contents from {src_dir} to {dest_dir}")

def generate_page(from_path, template_path, dest_path):
    import logging

    logging.info(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r', encoding='utf-8') as f:
        markdown = f.read()
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    html_content = markdown_to_html(markdown)
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(template)
    logging.info(f"Created HTML PAGE")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    import logging

    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                md_path = os.path.join(root, file)
                rel_path = os.path.relpath(md_path, dir_path_content)
                html_filename = os.path.splitext(rel_path)[0] + ".html"
                html_path = os.path.join(dest_dir_path, html_filename)

                # Create necessary directories in destination path
                os.makedirs(os.path.dirname(html_path), exist_ok=True)

                generate_page(md_path, template_path, html_path)

def main():
    copydir()
    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="public"
    )
main()