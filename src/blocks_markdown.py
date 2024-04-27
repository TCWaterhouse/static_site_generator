def markdown_to_blocks(markdown):
    init_blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in init_blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks