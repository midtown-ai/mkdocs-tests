from mkdocs.plugins import BasePlugin
from markdown.preprocessors import Preprocessor
import re


class YouTubeEmbedPreprocessor(Preprocessor):
    YOUTUBE_REGEX = re.compile(r"{%\s*youtube\s+(https?://www\.youtube\.com/watch\?v=([\w-]+)(?:&[^\s]+)?)\s*%}")

    def run(self, lines):
        new_lines = []
        for line in lines:
            match = self.YOUTUBE_REGEX.search(line)
            if match:
                video_url = match.group(1)
                video_id = match.group(2)
                iframe = (
                    f'<iframe width="560" height="315" '
                    f'src="https://www.youtube.com/embed/{video_id}" '
                    f'title="YouTube video player" frameborder="0" '
                    f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
                    f'referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
                )
                line = self.YOUTUBE_REGEX.sub(iframe, line)
            new_lines.append(line)
        return new_lines


class YouTubeEmbedPlugin(BasePlugin):
    def on_page_markdown(self, markdown, **kwargs):
        # Use the custom preprocessor to parse markdown
        preprocessor = YouTubeEmbedPreprocessor()
        return "\n".join(preprocessor.run(markdown.splitlines()))

