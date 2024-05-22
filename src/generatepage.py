import os

from blocks_markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")       

def read_file(path):
    with open(path) as p:
        return p.read()
        
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown = read_file(from_path)
    template = read_file(template_path)
    
    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()
    title = extract_title(markdown)
    
    final_html = template.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html)
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as p:
        p.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        file_name = filename.split(".")
        file_name = file_name[0]
        dest_file_name = file_name + ".html"
        dest_file_path = os.path.join(dest_dir_path, dest_file_name)
        if os.path.isfile(from_path):
            generate_page(from_path, template_path, dest_file_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)