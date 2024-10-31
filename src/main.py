# main.py

import shutil
import os
import logging
from block_markdown import markdown_to_blocks, markdown_to_html_node


def main():
    source_directory = "./static/"
    target_directory = "./public/"

    refresh_directory(source_directory, target_directory)

    # generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")


# configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def clear_directory(dir_path):
    if os.path.exists(dir_path):
        for file_name in os.listdir(dir_path):
            file_path = os.path.join(dir_path, file_name)
            if os.path.isdir(file_path):
                clear_directory(file_path)
                os.rmdir(file_path)
                logging.info(f"Removed Directory: {file_path}")
            else:
                os.remove(file_path)
                logging.info(f"Deleted file: {file_path}")


def copy_directory(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
        logging.info(f"Created Directory: {dest}")
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isdir(src_path):
            copy_directory(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)
            logging.info(f"Copied file from {src_path} to {dest_path}")


def refresh_directory(source_dir, target_dir):
    clear_directory(target_dir)
    copy_directory(source_dir, target_dir)


def extract_title(markdown):
    blocks = []
    trimmed_blocks = markdown_to_blocks(markdown)
    for block in trimmed_blocks:
        if block.startswith("# "):
            blocks.append(block)
    markdown_extract = blocks[0]
    markdown_extract = markdown_extract.lstrip("# ")
    markdown_extract = markdown_extract.rstrip(" ")
    return markdown_extract


sample_markdown = """   # This is a heading!

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

>Quotes are here
>and here

```plus = we have some code
and some more code```

This is text with a ![image](https://image.com/pic.gif) and ![kitty](https://cat.gov/zazzy.gif)

This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)

![image](https://image.com/pic.gif) and ![kitty](https://cat.gov/zazzy.gif)


* This is the **first list item** in a list block
* This is a *list item*
* This is another list item

1 This is an ordered list
2 This is second item of ordered list

This is another paragraph.

##### This is a closing heading, I think?

"""


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    with open(f"./{from_path}", encoding="utf-8") as markdown_file:
        markdown_data = markdown_file.read()
    with open(f"./{template_path}", encoding="utf-8") as template_file:
        template_data = template_file.read()
    markdown_to_html = markdown_to_html_node(markdown_data)  # .to_html()
    title = extract_title(markdown_data)
    content_in_template = template_data.replace("{{ Title }}", title)
    content_in_template = content_in_template.replace("{{ Content }}", markdown_to_html)

    with open(f"./{dest_path}", "w", encoding="utf-8") as content:
        content.write(content_in_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    with open(f"./{template_path}", encoding="utf-8") as template_file:
        template_data = template_file.read()
    dir_entries = os.listdir(path=f"./{dir_path_content}")
    for entry in dir_entries:
        full_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(full_path) and entry.endswith(".md"):
            with open(full_path, encoding="utf-8") as markdown_file:
                markdown_data = markdown_file.read()

            markdown_to_html = markdown_to_html_node(markdown_data).to_html()
            print(markdown_to_html)
            title = extract_title(markdown_data)

            content_in_template = template_data.replace("{{ Title }}", title)
            content_in_template = content_in_template.replace(
                "{{ Content }}", markdown_to_html
            )

            html_filename = entry.replace(".md", ".html")
            output_path = os.path.join(dest_dir_path, html_filename)

            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))
            with open(output_path, "w", encoding="utf-8") as content:
                content.write(content_in_template)

        elif os.path.isdir(full_path):
            generate_pages_recursive(
                full_path, template_path, os.path.join(dest_dir_path, entry)
            )


if __name__ == "__main__":
    main()
