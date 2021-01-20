#!/usr/bin/env python3
import os
import sys
import getopt
from settings import settings
from generator import gen_prevs, writer
from pathlib import Path


def main(argv):
    """main function
    """
    try:
        opts, args = getopt.getopt(argv, "h:g:n")
    except getopt.GetoptError:
        print('test.py -g to generate new blog page')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -g to generate new blog page')
            sys.exit()
        elif opt == '-g':
            # get the class of the parent container
            blog_class = s.preview_class()
            print("generating previews....")
            previews = gen_prevs(paths, title_tag, preview_tag, max_char, posts_dir)

            print("Writing to file...")
            new_file = writer(previews, blog_file, blog_class)

            # new blog file with the added previews
            blog_path.unlink()
            blog_path.touch()
            blog_path.write_text(new_file)
            print("Done.")


s = settings()

# load settings
try:
    title_tag = s.preview_title_tag()
except Exception as e:
    raise e
    print("check settings file for title_tag value")
    sys.exit(2)

try:
    preview_tag = s.preview_content_tag()
except Exception as e:
    raise e
    print("check settings file for preview_content_tag value")
    sys.exit(2)

try:
    max_char = s.preview_max_char()
except Exception as e:
    raise e
    print("check settings file for max_char value")
    sys.exit(2)

try:
    posts_dir = s.posts_dir()
except Exception as e:
    raise e
    print("check settings file for posts_dir value")
    sys.exit(2)

# lists contents of posts by date


try:
    dirpath = s.web_dir()+s.posts_dir()
except Exception as e:
    raise e
    print("check settings file for web_dir value")
    sys.exit(2)


try:
    paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)
except Exception as e:
    raise e
    print("make sure the path for the posts directory exists")
    sys.exit(2)

# open the blog file


try:
    blog_path = Path(s.web_dir()+s.blog_page())
except Exception as e:
    raise e
    print("check settings file for blog_page value")
    sys.exit(2)

blog_file = blog_path.read_text()

if __name__ == "__main__":
    main(sys.argv[1:])
