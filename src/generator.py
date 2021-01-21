from bs4 import BeautifulSoup
from pathlib import Path


def gen_prevs(paths, title_tag, preview_tag, max_char, posts_dir):
    """generate post preview from each blog file
    :returns: list of post previews

    """

    posts = []
    for page in paths:
        linkp = str(page)
        posts.append([Path(page).read_text(), linkp[linkp.find(posts_dir):]])

    previews = []
    for post in posts:

        soup = BeautifulSoup(post[0], 'html.parser')

        prev = soup.p
        title = soup.title
        link = soup.new_tag("a", href=post[1])

        # replace title tag with new tag
        title.name = title_tag

        # replace p tag with the new tag
        prev.name = preview_tag

        link.extend(title)
        # summarization of p
        max_char = int(max_char)
        char_len = len(prev.string)

        if char_len > max_char:
            prev.string = prev.string[0:max_char]
            prev.string = prev.string+"..."
        previews.append([link, prev])
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


def new(title, web_dir, posts_dir, post_template):
    """ generate new blog page and put title there
    """

    temp_path = Path(web_dir+post_template)
    template = temp_path.read_text()
    soup = BeautifulSoup(template, 'html.parser')
    name = soup.title
    name.clear()
    name.extend(title)
    new_file = "/"+title+".html"
    new_path = web_dir+posts_dir+new_file
    Path(new_path).touch()
    Path(new_path).write_text(str(soup))
    return new_path
