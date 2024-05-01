block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    init_blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in init_blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")
    headings = "# ", "## ", "### ", "#### ", "##### ", "###### "
    if block.startswith(headings):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if all(line.startswith(">") for line in lines):
        return block_type_quote
    if all(line.startswith("* ") for line in lines):
        return block_type_unordered_list
    if all(line.startswith("- ") for line in lines):
        return block_type_unordered_list
    for i in range(len(lines)):
        if lines[i].startswith(f"{i + 1}. "):
            if i == len(lines) - 1:
                return block_type_ordered_list
            continue
        else:
            break
    return block_type_paragraph