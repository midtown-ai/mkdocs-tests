import logging
import os

from glob import iglob
from mkdocs.config.defaults import MkDocsConfig
from pathspec.gitignore import GitIgnoreSpec
from zipfile import ZipFile, ZIP_DEFLATED

# -----------------------------------------------------------------------------
# State
# -----------------------------------------------------------------------------

# Initialize incremental builds
is_serve = False

# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

# Determine whether we're serving the site
def on_startup(command, dirty):
    global is_serve
    is_serve = command == "serve"

# Create archives for all examples
def on_post_build(config: MkDocsConfig):
    if is_serve:
        return

    # Read files to ignore from .gitignore
    with open(".gitignore") as f:
        spec = GitIgnoreSpec.from_lines([
            line for line in f.read().split("\n")
                if line and not line.startswith("#")
        ])

    # Create archives for each example
    for file in iglob("examples/*/mkdocs.yml", recursive = True):
        base = os.path.dirname(file)

        # Compute archive name and path
        example = os.path.basename(base)
        archive = os.path.join(config.site_dir, f"{example}.zip")

        # Start archive creation
        log.info(f"Creating archive '{example}.zip'")
        with ZipFile(archive, "w", ZIP_DEFLATED, False) as f:
            for name in spec.match_files(os.listdir(base), negate = True):
                path = os.path.join(base, name)
                if os.path.isdir(path):
                    path = os.path.join(path, "**")

                # Find all files recursively and add them to the archive
                for file in iglob(path, recursive = True, include_hidden = True):
                    log.debug(f"+ '{file}'")
                    f.write(file, os.path.join(
                        example, os.path.relpath(file, base)
                    ))

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------

# Set up logging
log = logging.getLogger("mkdocs.material.examples")

# https://github.com/mkdocs-material/examples/tree/master/hooks
