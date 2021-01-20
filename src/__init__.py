#!/usr/bin/env python3
import os
from settings import settings
from generator import gen_prevs
from generator import writer
from pathlib import Path

s = settings()

# load settings
title_tag = s.preview_title_tag()
preview_tag = s.preview_content_tag()
max_char = s.preview_max_char()
posts_dir = s.posts_dir()

# lists contents of posts by date
dirpath = s.web_dir()+s.posts_dir()
paths = sorted(Path(dirpath).iterdir(), key=os.path.getmtime)

# open the blog file
blog_path = Path(s.web_dir()+s.blog_page())
blog_file = blog_path.read_text()

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
