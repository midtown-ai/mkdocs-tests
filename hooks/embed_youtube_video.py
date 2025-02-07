import logging
import re
import os

log = logging.getLogger('mkdocs')

# Debugging configuration
DEBUG = os.getenv("YOUTUBE_HOOK_ENABLED", "True").lower() in ("false", "0", "no")  # Controlled via environment variable
DEBUG_PAGE_URL_FILTER = re.compile(r"tests/youtube_hook/")  # Filter specific pages for debugging
YOUTUBE_REGEX_STR = r"{%\s*youtube\s+\"(https?://www\.youtube\.com/watch\?v=([\w-]+)(?:&t=(\d+))?.*?)\"\s*(.*?)\s*%}"

def debug_log(message):
    """Helper to log debug messages if DEBUG is enabled."""
    if DEBUG:
        log.warning(message)

def youtube_url_to_iframe(markdown):
    """
    Parses a Markdown string and replaces all occurrences of
    {% youtube URL %} with the corresponding YouTube iframe embed code.

    Supports Markdown attr_list to customize iframe attributes.

    Parameters:
        markdown (str): The Markdown content containing {% youtube ... %}.

    Returns:
        str: The updated Markdown content with embedded YouTube iframes.
    """
    YOUTUBE_REGEX = re.compile(YOUTUBE_REGEX_STR)

    def replace_with_iframe(match):
        video_url = match.group(1)
        video_id = match.group(2)
        start_time = match.group(3)  # Time parameter (t)
        attributes = match.group(4).strip()   # Attribute passed in the markdown element

        default_attrs = {
            "width": "560",
            "height": "315",
            "frameborder": "0",
            "allow": "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
            "referrerpolicy": "strict-origin-when-cross-origin",
            "allowfullscreen": "allowfullscreen"
        }

        # Parse additional attributes from attr_list if provided
        alignment = None
        if attributes:
            for attr in attributes.split():
                if "=" in attr:
                    key, value = attr.split("=", 1)
                    default_attrs[key] = value.strip('"')
                elif attr in ["center", "left", "right"]:
                    alignment = attr

        # Add start time to the embed URL if present
        embed_url = f"https://www.youtube.com/embed/{video_id}"
        if start_time:
            embed_url += f"?start={start_time}"

        # Build the iframe tag with custom and default attributes
        iframe_attrs = " ".join([f'{key}="{value}"' for key, value in default_attrs.items()])
        iframe_tag = f'<iframe src="{embed_url}" {iframe_attrs}></iframe>'

        # Align the iframe based on the specified alignment
        if alignment == "center":
            return f'<div style="display: flex; justify-content: center;">{iframe_tag}</div>'
        elif alignment == "left":
            return f'<div style="display: flex; justify-content: flex-start;">{iframe_tag}</div>'
        elif alignment == "right":
            return f'<div style="display: flex; justify-content: flex-end;">{iframe_tag}</div>'

        return iframe_tag

    return YOUTUBE_REGEX.sub(replace_with_iframe, markdown)

def on_page_markdown(markdown, **kwargs):
    """
    Markdown processing hook for MkDocs.
    """
    page = kwargs['page']

    # Debug-specific processing
    if DEBUG:
        # Process only selected pages when debugging
        if not DEBUG_PAGE_URL_FILTER.match(page.url):
            return markdown

        path = page.file.src_uri
        matches = re.finditer(YOUTUBE_REGEX_STR, markdown)
        for match in matches:
            youtube_markdown = match.group(0)
            youtube_url = match.group(1)
            video_id = match.group(2)
            debug_log(f"Found YouTube markdown in '{path}': {youtube_markdown}")
            debug_log(f"- YouTube URL: {youtube_url}")
            debug_log(f"- Video ID: {video_id}")

    # Process the markdown
    updated_markdown = youtube_url_to_iframe(markdown)

    # Debug final result
    debug_log("Updated Markdown content:")
    debug_log(updated_markdown)

    return updated_markdown

# Example Usage
if __name__ == "__main__":
    example_markdown = """
    Here is an embedded YouTube video:
    {% youtube "https://www.youtube.com/watch?v=zU6eovES53M&t=420s" width="800" height="450" %}
    in a div
    {% youtube "https://www.youtube.com/watch?v=zU6eovES53M&t=420s" width="800" height="450" center %}
    Another video aligned left:
    {% youtube "https://www.youtube.com/watch?v=dQw4w9WgXcQ" right %}
    """

    updated_markdown = youtube_url_to_iframe(example_markdown)
    print(updated_markdown)
