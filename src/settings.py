import toml
import os


class settings:

    """Read settings from toml file"""

    def __init__(self):
        self.settings_path = os.environ['GRAFF_CONF']
        self.tomlf = toml.load(self.settings_path)

    def web_dir(self):
        # returns website directory
        return self.tomlf["files"]["web_dir"]

    def posts_dir(self):
        # returns posts directory
        return self.tomlf["files"]["posts_dir"]

    def blog_page(self):
        # returns page to put blog previews
        return self.tomlf["files"]["blog_page"]

    def preview_class(self):
        # returns class of the parent element of the blog previews
        return self.tomlf["blog"]["preview_class"]

    def preview_container_tag(self):
        # returns class of the parent element of the blog previews
        return self.tomlf["blog"]["preview_container_tag"]

    def preview_tag(self):
        # returns class of the parent element of the blog previews
        return self.tomlf["blog"]["preview_tag"]

    def preview_title_tag(self):
        # returns class of the parent element of the blog previews
        return self.tomlf["blog"]["preview_title_tag"]

    def preview_content_tag(self):
        # returns class of the parent element of the blog previews
        return self.tomlf["blog"]["preview_content_tag"]

    def preview_max_char(self):
        # returns the preview content max characters before ending with "..."
        return self.tomlf["blog"]["preview_max_char"]
