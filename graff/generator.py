import os
from settings import settings
from bs4 import BeautifulSoup
from pathlib import Path

s = settings()

title_tag = s.preview_title_tag()
preview_tag = s.preview_content_tag()

# lists contents of posts by date
dirpath = s.web_dir()+s.posts_dir()
paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)

# open the blog file
blog_path = Path(s.web_dir()+s.blog_page())
blog_file = blog_path.read_text()

# get the class of the parent container
blog_class = s.preview_class()


def gen_prevs(paths, title_tag, preview_tag):
    """generate post preview from each blog file
    :returns: list of post previews

    """
    s = settings()

    posts = []
    for page in paths:
        posts.append(Path(page).read_text())

    previews = []

    for post in posts:

        soup = BeautifulSoup(post, 'html.parser')

        prev = soup.p
        title = soup.title

        # replace title tag with new tag
        title.name = title_tag

        # replace p tag with the new tag
        prev.name = preview_tag

        # summarization of p
        max_char = int(s.preview_max_char())
        char_len = len(prev.string)

        if char_len > max_char:
            prev.string = prev.string[0:max_char]
            prev.string = prev.string+"..."
        previews.append([title, prev])
    return previews


def wirter(previews, blog_file, blog_class):
    """Write the previews to the selecte file
    """

    soup = BeautifulSoup(blog_file, 'html.parser')
    _class_ = soup.find(class_=blog_class)
    _class_.clear()
    for preview in previews:
        li = soup.new_tag('li')
        li.extend(preview)
        _class_.append(li)
    return soup.prettify()


previews = gen_prevs(paths, title_tag, preview_tag)
new_file = wirter(previews, blog_file, blog_class)
blog_path.unlink()
blog_path.touch()
blog_path.write_text(new_file)
print(paths)
