---
template: main.html
title: Material for MkDocs
social:
  cards_layout_options:
    title: Documentation that simply works
    
# next_page:
#     url: tracks/index.md
#     title: "Educational Track"
---

## plugins

```python
# config.py file

from mkdocs.config.base import Config

# from mkdocs.config.config_options import Deprecated, Type

class MyPluginConfig(Config):
    enabled = Type(bool, default = True)

    cards = Type(bool, default = True)
    cards_dir = Type(str, default = "assets/images/social")
    cards_layout_options = Type(dict, default = {})

#   cards_color = Deprecated(
#       option_type = Type(dict, default = {}),
#       message =
#           "Deprecated, use 'cards_layout_options.background_color' "
#           "and 'cards_layout_options.color' with 'default' layout"
#   )
```

Source - https://github.com/squidfunk/mkdocs-material/blob/master/src/plugins/social/config.py

```python
# plugin.py file

from mkdocs.plugins import BasePlugin

from .config import SocialConfig

class MyPluginPlugin(BasePlugin[MyPluginConfig]):

    def __init__(self):

    # ---------------------------- Retrieve configuration ------------------------------
    def on_config(self, config):

        # Move color options (Deprecated)
        if self.config.cards_color:

    # ---------------------------- Create social cards  ---------------------------------
    def on_page_content(self, html, page, config, files):

        # Compute page title and description
        title = page.meta.get("title", page.title)
        description = config.site_description or ""
        if "description" in page.meta:
            description = page.meta["description"]

    # ---------------------------- Check results of executors ---------------------------
    def on_post_build(self, config):
        if not self.config.cards:
            return

        # Check for exceptions
        for promise in self._image_promises:
            promise.result()

    # -------------------------------------------------------------------------

```

## Events / Hooks

| Configuration and Setup Events | Description |
|--------------------------------|-------------|
| on_config(config)	             | Called after the config is loaded and validated. Modify or inspect the configuration here. |
| on_pre_build(config)	         | Called before any build actions are taken. Good for setup tasks. |
| on_files(files, config)	     | Called after files are collected but before being processed. You can add, remove, or modify files here. |
| on_nav(nav, config, files)     | Called after navigation is created. Can be used to modify the site structure. |
| on_env(env, config, files)     | Called after the Jinja2 environment is created. Useful for adding custom filters or globals. |

| Page-level Events              | Description |
|--------------------------------|-------------|
| on_page_markdown(markdown, page, config, files) | Called after the markdown source is read but before conversion. Great for preprocessing markdown. |
| on_page_content(html, page, config, files)      | Called after markdown is converted to HTML, but before being passed to the template. |
| on_page_context(context, page, config, nav)     | Called before a page is rendered. You can modify the Jinja2 context here. |
| on_post_page(output, page, config)              | Called after the page is rendered and HTML is generated. Can be used to post-process HTML or store metadata. |

| Build & Output Events          | Description |
|--------------------------------|-------------|
| on_post_build(config)                        | Called after the site is built but before files are written to disk. Useful for cleanup or final analysis. |
| on_post_build_environment(env, config)       | Called after build environment is finalized. Useful for teardown. |
| on_post_build_site(config)                   | Called after everything has been built and written. Rarely used, but useful for post-processing outputs. |
| on_post_build_commands(config)               | Called after shell commands in the config are executed. |
| on_serve(server, config, builder)            | Called when running mkdocs serve. Allows you to modify the dev server. |
| on_pre_template(context)                     | Internal use; rarely needed. |
| on_post_template(context)                    | Internal use; rarely needed. |
| on_page_read_source(path, config)            | If you want to override how a page source is read (e.g., dynamic content). |


### Event workflow

```
on_config
   ↓
on_pre_build
   ↓
on_files
   ↓
on_nav
   ↓
on_env
   ↓
 ┌────────────────────────────┐
 │    For each page           │
 │                            │
 │ → on_page_markdown         │
 │ → on_page_content          │
 │ → on_page_context          │
 │ → on_post_page             │
 └────────────────────────────┘
   ↓
on_post_build
```

### on_page_markdown

Called after the markdown source is read but before conversion. Great for preprocessing markdown.

#### ReplaceTOCPlugin

Plugin Code

```
from mkdocs.plugins import BasePlugin

class ReplaceTOCPlugin(BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        # Replace a custom placeholder with a fixed string
        updated_markdown = markdown.replace('{{TOC}}', '**Table of Contents will go here**')
        return updated_markdown
```

Configuration (mkdocs.yml snippets)

```
plugins:
  - search
  - replace-toc:
      enabled: true

plugins_dir: plugins
```

Input markdown file example

```
# Welcome

{{TOC}}

Some more content here.
```

Expected markdown output

```
# Welcome

**Table of Contents will go here**

Some more content here.
```


### on_page_context

Called before a page is rendered. You can modify the Jinja2 context here.

#### SourcePagePlugin

This plugin will:

 * Access page.file during the on_page_context event.
 * Extract the source file path (src_uri) and destination URL (url).
 * Inject it into the page context so you can use it in your templates.

```
# Create a plugin in plugins/source_path.py:

from mkdocs.plugins import BasePlugin

class SourcePathPlugin(BasePlugin):

    def on_page_context(self, context, page, config, nav, **kwargs):
        file = page.file

        # Extract info from page.file
        source_info = {
            'abs_src_path': file.abs_src_path,
            'src_uri': file.src_uri,
            'dest_uri': file.dest_uri,
            'url': file.url,
            'name': file.name,
            'edit_url': file.edit_url
        }

        # Add it to the context
        context['source_info'] = source_info

        return context
```

```
# Update mkdocs.yml to register the plugin:

plugins:
  - search
  - source-path:
      enabled: true

# If your plugin is not pip-installed, point to the file:
plugins_dir: plugins
```

```
# Use it in your custom theme (Jinja2 template):
# Inside your main.html or a custom page.html, insert:

{% if source_info %}
<div class="source-debug">
    <h4>Page Debug Info</h4>
    <ul>
        <li><strong>Source file:</strong> {{ source_info.src_uri }}</li>
        <li><strong>Destination URL:</strong> {{ source_info.url }}</li>
        <li><strong>Edit URL:</strong> <a href="{{ source_info.edit_url }}">{{ source_info.edit_url }}</a></li>
    </ul>
</div>
{% endif %}
```

### on_page_content event

Called after markdown is converted to HTML, but before being passed to the template.

This is great for:

  * Adding disclaimers
  * Inserting custom banners
  * Tracking tags (like analytics)
  * Warnings or notices

#### FooterInjector Plugin

Appends a custom HTML footer to every page's content, after Markdown has been converted to HTML but before the template is applied.

```
from mkdocs.plugins import BasePlugin

class FooterInjectorPlugin(BasePlugin):
    def on_page_content(self, html, page, config, files):
        # Define the custom HTML you want to inject
        footer_html = """
        <div style="margin-top: 2em; padding: 1em; border-top: 1px solid #ccc; font-size: 0.9em; color: gray;">
            <p>📘 Documentation generated by MkDocs.</p>
            <p>Last updated: {{ page.meta.last_updated if page.meta.last_updated else "unknown" }}</p>
        </div>
        """
        # Append the HTML footer to the end of the page's content
        return html + footer_html

```

## External references

 * https://github.com/hmasdev/mkdocs-material-extended-social-plugin/tree/main/mkdocs_material_extended_social_plugin
