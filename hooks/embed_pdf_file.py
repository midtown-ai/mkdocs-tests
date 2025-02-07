import logging
import re
import os

log = logging.getLogger('mkdocs')

# Debugging configuration
DEBUG = os.getenv("PDF_HOOK_ENABLED", "True").lower() in ("false", "0", "no")  # Controlled via environment variable
DEBUG_PAGE_URL_FILTER = re.compile(r"tests/pdf_hook/")  # Filter specific pages for debugging
PDF_REGEX_STR = r"{%\s*pdf\s+\"(https?://[^\"]+)\"\s*(.*?)\s*%}"

def debug_log(message):
    """Helper to log debug messages if DEBUG is enabled."""
    if DEBUG:
        log.warning(message)

def pdf_url_to_object(markdown):
    """
    Parses a Markdown string and replaces all occurrences of
    {% pdf URL %} with the corresponding HTML object embed code.

    Supports Markdown attr_list to customize object attributes.

    Parameters:
        markdown (str): The Markdown content containing {% pdf ... %}.

    Returns:
        str: The updated Markdown content with embedded PDF objects.
    """
    PDF_REGEX = re.compile(PDF_REGEX_STR)

    def replace_with_object(match):
        pdf_url = match.group(1)
        attributes = match.group(2).strip()  # Attribute passed in the markdown element

        # Default attributes for the <object> tag
        default_attrs = {
            "type": "application/pdf",
            "width": "100%",
            "height": "600px"
        }

        # Parse additional attributes from attr_list if provided
        if attributes:
            for attr in attributes.split():
                if "=" in attr:
                    key, value = attr.split("=", 1)
                    default_attrs[key] = value.strip('"')

        # Build the HTML object tag
        object_attrs = " ".join([f'{key}="{value}"' for key, value in default_attrs.items()])
        object_html = (
            f'<object data="{pdf_url}" {object_attrs}>\n'
            f'    <p>Your browser does not support PDFs. Please download the PDF: \n'
            f'       <a href="{pdf_url}">Download PDF</a>.\n'
            f'    </p>\n'
            f'</object>'
        )
        return object_html

    return PDF_REGEX.sub(replace_with_object, markdown)

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
        matches = re.finditer(PDF_REGEX_STR, markdown)
        for match in matches:
            pdf_markdown = match.group(0)
            pdf_url = match.group(1)
            debug_log(f"Found PDF markdown in '{path}': {pdf_markdown}")
            debug_log(f"- PDF URL: {pdf_url}")

    # Process the markdown
    updated_markdown = pdf_url_to_object(markdown)

    # Debug final result
    debug_log("Updated Markdown content:")
    debug_log(updated_markdown)

    return updated_markdown

# Example Usage
if __name__ == "__main__":
    example_markdown = """
    Here is an embedded PDF:
    {% pdf "https://arxiv.org/pdf/2411.14251v1" width="80%" height="500px" %}
    """

    updated_markdown = pdf_url_to_object(example_markdown)
    print(updated_markdown)

