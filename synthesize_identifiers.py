"""
Identifier Synthesis Script
Input: directory filled with reports which have had identifiers removed and replaced with tags
Output: directory of those reports where identifier tags have been replaced with realistic synthetic identifiers

Calling the Script
Arguments: src_folder output_folder
"""

import argparse
import os
import re

from Globals import *
from Packages.TagReplacer import TagReplace
from Packages.GeographicalTagReplacerMethods import Address     # needed to read address pickle file


def main(src_folder, output_folder):
    tag_replacer = TagReplace()

    # for each file in src folder
    for src_filename in os.listdir(src_folder):

        # open source and target files
        src_file_path = os.path.join(src_folder, src_filename)
        out_file_path = os.path.join(output_folder, src_filename)

        create_resynthesized_file(src_file_path, out_file_path, tag_replacer)


def create_resynthesized_file(src_file_path, out_file_path, tag_replacer):
    # input de-identified report
    with open(src_file_path, "r") as src_file:
        src_lines = src_file.readlines()

    # resynthesize report
    target_lines = replace_tags_for_document(src_lines, tag_replacer)

    # output resynthesized report
    with open(out_file_path, "w") as out_file:
        out_file.writelines(target_lines)


def replace_tags_for_document(src_lines, tag_replacer):
    target_lines = []

    for index, src_line in enumerate(src_lines):
        if TAG_MARKER not in src_line:
            target_lines.append(src_line)
        else:
            resynthezied_line = replace_tags_for_line(src_line, tag_replacer)
            target_lines.append(resynthezied_line)

    return target_lines


def replace_tags_for_line(line, tag_replacer):
    resynthesized_line = line
    offset = 0
    across_tag_info = {}

    # iterate over each tag in the sentence
    for star_star in re.finditer("\*\*", line):

        # Determine type of tag, if any
        star_start, tag_name_start = star_star.span()

        is_tag_like = re.match("[\w\-]+", line[tag_name_start:])
        if is_tag_like:
            tag = is_tag_like.group(0)
            tag_name_end = tag_name_start + is_tag_like.span()[1]

            # If it's a tag, replace according to which tag it is
            if tag in TAGS:
                # Find method to use based on tag -- in Packages/TagReplacer.py
                tag_replacer_method_name = REPLACE_METHOD_NAME + TAG_VARIABLES[tag]
                tag_replacer_method = getattr(tag_replacer, tag_replacer_method_name)

                # adjust for offset between original line and resynthesized line
                star_start += offset
                tag_name_end += offset

                # replace tag
                resynthesized_line, additional_offset = tag_replacer_method(resynthesized_line, star_start,
                                                                            tag_name_end, across_tag_info)
                offset += additional_offset

    return resynthesized_line


if __name__ == '__main__':
    # Arguments:    src_folder target_folder
    parser = argparse.ArgumentParser()
    source_folder = "source_folder"
    output_folder = "output_folder"

    parser.add_argument(source_folder, help="the input file name")
    parser.add_argument(output_folder, help="name of language to translate into: 'eng' or 'jap'")
    args = parser.parse_args()

    main(args.source_folder, args.output_folder)
