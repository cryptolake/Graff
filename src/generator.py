from bs4 import BeautifulSoup
from pathlib import Path


def gen_prevs(paths, title_tag, preview_tag, max_char):
    """generate post preview from each blog file
    :returns: list of post previews

    """

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
        max_char = int(max_char)
        char_len = len(prev.string)

        if char_len > max_char:
            prev.string = prev.string[0:max_char]
            prev.string = prev.string+"..."
        previews.append([title, prev])
    return previews


def writer(previews, blog_file, blog_class):
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
