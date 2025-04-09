---
template: main.html
title:  Paying with Jinja
# social:
#   cards_layout_options:
#     title: Documentation that simply works
    
# next_page:
#     url: tracks/index.md
#     title: "Educational Track"
---

## Getting objects and attributes

```
{{ base_url }}              - relative path from the current page to the root of the site (where ./docs is located)

# Examples
<link rel="stylesheet" href="{{ base_url }}/assets/css/custom.css">
```

```
{{ config.plugins }}        - List of plugins
{{ config.site_name }}      - value of the site_name parameter in the configuration file (mkdocs.yml)
{{ config.site_url }}       - value of the site_url parameter in the configuration file (mkdocs.yml) OR http://127.0.0.1:<port> when running locally
{{ config.theme.locale }}
{{ config.theme.locale.language }}

{{ config.extra.version }}
{{ config.extra.links }}

# Examples
```

```
{{ link.title }}
{{ link.url }}
{{ link.children }}
{{ link.active }}
{{ link.is_link }}
{{ link.is_page }}
{{ link.is_section }}

# Examples
```

```
{{ page.abs_url }}            - value of the URL path after the site_url
{{ page.active }}             - True if is currently viewed page
{{ page.canonical_url }}      - The full URL to the page
{{ page.children }}           - 
{{ page.edit_url }}           - URL to the source page in the source repository
{{ page.file }}               - represents the underlying source page
{{ page.file.abs_dest_path }} - absolute path where the output HTML file will be written.
{{ page.file.abs_src_path }}  - abs path to source markdown file
{{ page.file.dest_uri }}      - destination URI (relative to the site root), typically ending in .html.
{{ page.file.edit_url }}      - edit URL if edit_uri is configured in mkdocs.yml. Useful for GitHub integration.
{{ page.file.name }}          - base name of the file without extension (e.g., index for index.md).
{{ page.file.page }}          - reference to the page object itself (recursive, but usually not used).
{{ page.file.src_uri }}       - path to the source file, relative to the documentation directory.
{{ page.file.url }}           - final rendered URL of the page in the site (e.g., about/).
{{ page.is_homepage }}        - True if home page of site
{{ page.is_link }}            - False for page objects, True for link objects
{{ page.is_section }}         - False for a page objects. Useful for iteration on navigation bar
{{ page.meta.title }}         - value of the title in the page's YAML front matter
{{ page.next_page }}          - next page (Page object) based on the site navigation
{{ page.parent }}             - Immediate parent (Section object) in the site navigation
{{ page.previous_page }}      - previous page (Page object) based on the site navigation
{{ page.title }}              - value of either (1) title in front matter, (2) first-level heading in markdown content, (3) name in nav: entry in mkdocs.yml
{{ page.url | url }}          - URL of the page relative to the mkdocs site_dir
{{ page.content }}

# Examples
```

```
{{ section.parent }}
{{ section.title }}
{{ section.children }}
{{ section.active }}
{{ section.is_section }}
{{ section.is_page }}
{{ section.is_link }}

# Examples
```

```
# Jinja2 variables


{{ direction }}               - value of a jinja variable

{% set _ = ... %}             - _ a temporary variable name
_.value = something
{{ _.value }}                 - outputs of a stored value in a field
```

## Functions

```
{{ super() }}                 - calls the content of the block as defined in the parent template
                              - used to add or modify a block content, rather than replace it

{% block extrahead %}
  {{ super() }}
  <link rel="stylesheet" href="{{ 'styles/custom.css' | url }}">
{% endblock %}

```

```
# Translation
# translation file is by default overrides/partials/languages/en.html
title="{{ lang.t('search.reset') }}"  - inserts the translated string for search.reset into the HTML title attribute
```

```
{% set _ = namespace() %}   - create a mutable object for reuse

{% set icon = config.theme.icon.share or "material/share-variant" %}
```


## Directives

```
{% extends "base.html" %}   - use the base.html Jinja template to inherit from

{% block extrahead %}       - replace the block extrahead in base.html with the following content before rendering
    some HTML
{% endblock %}

```

More at https://jinja.palletsprojects.com/en/latest/templates/#template-inheritance

```
{% include "partials/javascripts/announce.html" %}   - include a partial HTML file
```

```

<!-- This is an HTML comment which will appear in the generated HTML output -->

{#- Beginning of multi-line comment in Jinja template only

-#}
```

### macros imports

```
# https://github.com/squidfunk/mkdocs-material/blob/master/src/templates/partials/language.html
<!-- Import translations for given language and fallback -->
{% import "partials/languages/" ~ config.theme.language ~ ".html" as lang %}
{% import "partials/languages/en.html" as fallback %}

<!-- Re-export translations -->
{% macro t(key) %}{{ lang.t(key) or fallback.t(key) or key }}{% endmacro %}
```

```
# https://github.com/squidfunk/mkdocs-material/blob/master/src/templates/partials/languages/en.html
{% macro t(key) %}{{ {
  "language": "en",
  "direction": "ltr",
  "action.edit": "Edit this page",
  "action.skip": "Skip to content",
  "action.view": "View source of this page",
  "announce.dismiss": "Don't show this again",
  "blog.archive": "Archive",
  "blog.categories": "Categories",
  "blog.categories.in": "in",
  "blog.continue": "Continue reading",
  "blog.draft": "Draft",
  "blog.index": "Back to index",
  "blog.meta": "Metadata",
  "blog.references": "Related links",
  "clipboard.copy": "Copy to clipboard",
  "clipboard.copied": "Copied to clipboard",
  "consent.accept": "Accept",
  "consent.manage": "Manage settings",
  "consent.reject": "Reject",
  "footer": "Footer",
  "footer.next": "Next",
  "footer.previous": "Previous",
  "header": "Header",
  "meta.comments": "Comments",
  "meta.source": "Source",
  "nav": "Navigation",
  "readtime.one": "1 min read",
  "readtime.other": "# min read",
  "rss.created": "RSS feed",
  "rss.updated": "RSS feed of updated content",
  "search": "Search",
  "search.config.lang": "en",
  "search.config.pipeline": "stopWordFilter",
  "search.config.separator": "[\\s\\-]+",
  "search.placeholder": "Search",
  "search.share": "Share",
  "search.reset": "Clear",
  "search.result.initializer": "Initializing search",
  "search.result.placeholder": "Type to start searching",
  "search.result.none": "No matching documents",
  "search.result.one": "1 matching document",
  "search.result.other": "# matching documents",
  "search.result.more.one": "1 more on this page",
  "search.result.more.other": "# more on this page",
  "search.result.term.missing": "Missing",
  "select.language": "Select language",
  "select.version": "Select version",
  "source": "Go to repository",
  "source.file.contributors": "Contributors",
  "source.file.date.created": "Created",
  "source.file.date.updated": "Last update",
  "tabs": "Tabs",
  "toc": "Table of contents",
  "top": "Back to top"
}[key] }}{% endmacro %}
```

### If-then-else

```
{% if config.theme.palette %}
    <body
      dir="{{ direction }}"
      data-md-color-scheme="{{ scheme | replace(' ', '-') }}"
      data-md-color-primary="{{ primary | replace(' ', '-') }}"
      data-md-color-accent="{{ accent | replace(' ', '-') }}"
    >
{% else %}
    <body dir="{{ direction }}">
{% endif %}

# Other examples
{% set features = config.theme.features or [] %}
{% if "announce.dismiss" in features %}                - 
    ....
{% endif %}

{% if not palette is mapping %}
    {% set palette = palette | first %}
{% endif %}

{% if "toc.integrate" not in features %}

{% if page.meta and page.meta.hide %}

```

### For loop

```
extra:
  version: 0.13.0
  links:
    - https://github.com/mkdocs
    - https://docs.readthedocs.org/en/latest/builds.html#mkdocs
    - https://www.mkdocs.org/
```

```
{{ config.extra.version }}

{% if config.extra.links %}
  <ul>
  {% for link in config.extra.links %}
      <li>{{ link }}</li>
  {% endfor %}
  </ul>
{% endif %}
```

## Template Filters

```
{{ " Hello World! "|trim|lower|replace(" ", "-") }}
```

```
| capitalize                   - capitatlize the first character of the string

| default("fallback")          - d is an alias to default
| d("fallback")                - if variable is undefined or None, return "fallback"
| d("fallback", true)          - if variable is undefined or None or 0 or '', return "fallback"

| escape                       - escape HTML characters
| first
| float                        - converts a value to a float
| int
| join('-')                    - joins a list into a string
| length                       - returns the length of a string
| lower                        - converts to lowercase
| replace(' ', '-')
| reverse                      - reverses a list or string
| round(2)                     - rounds numbers
| safe                         - marks string as safe
| sort                         - sorts a list
| split(',')                   - splits a string into a list
| striptags                    - removes HTMl tags
| title                        - cpitalizes the first letter of each word
| tojson                       - turns a dictionary into a json object
| trim                         - removes heading and trailing white spaces
| unique                       - removes duplicate from a list
| upper                        - converts to uppercase
| url
| urlencode                    - URL-encodes a string
X urljoin
| wordcount                    - counts words in a string
```

Examples

```
{{ user_name | default('Guest') }}
```

```
{% set first_name = "John" %}
{% set last_name = "Doe" %}
{% set full_name = first_name ~ " " ~ last_name %}
{{ full_name }} {# Output: John Doe #}
```

```
{% set items = ["apple", "banana", "cherry"] %}
{{ items | join(", ") }} {# Output: apple, banana, cherry #}
```

```
/* Safely convert a python object to a value in a JavaScript script */
<script>
    var mkdocs_page_name = {{ page.title|tojson|safe }};
</script>
```

```
{% set image_relative_url = page.meta.image_file | url %}
{% set image_absolute_url = config.site_url ~ image_relative_url %}

<meta property="og:image" content="{{ image_absolute_url }}">

# OR

{% if page.meta.image_file and config.site_url %}
  <meta property="og:image" content="{{ config.site_url | trim('/') }}/{{ page.url | trim('/') }}/{{ page.meta.image_file }}">
{% endif %}

```

## references

 * Jinja - https://jinja.palletsprojects.com/en/latest/templates/#template-inheritance
