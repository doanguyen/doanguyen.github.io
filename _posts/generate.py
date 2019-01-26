# -*- coding: utf-8 -*-
import argparse
import os
import datetime
import slugify
import codecs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder to store the article')
    parser.add_argument('title', help='Title of the post, unicode supported')
    parser.add_argument('--tags')
    parser.add_argument('--summary')
    args = parser.parse_args()

    folder = os.path.join(os.path.dirname(__file__), args.folder)
    is_folder = os.path.isdir(folder)
    if not is_folder:
        raise Exception(f"Folder {folder} is not found")
    title = args.title
    date = datetime.datetime.now()
    summary = args.summary if args.summary else ""
    permalink = slugify.slugify(title)

    filename = f"{datetime.datetime.now().strftime('%Y-%m-%d')}-{permalink}.md"
    filename = os.path.join(folder, filename)
    tags = args.tags if args.tags else ""

    header_template = f"""---
layout:     post
title:     {title}
date:      {date}
summary:   {summary}
permalink:	{permalink}
tags: {tags}
---"""
    if os.path.isfile(filename):
        raise Exception("ERROR, file exist")
    with codecs.open(filename, 'w+', 'utf-8') as f:
        f.write(header_template)


if __name__ == "__main__":
    main()
