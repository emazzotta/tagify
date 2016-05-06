#!/usr/bin/env python3

import glob
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Parse YAML Front Matters and write according OSX file tags.')
parser.add_argument('-p', '-path', type=str,
                    help='Path to folder which contains markdown files.')

def tagFiles(filePath):
    tempTag = []
    tagCounter = 0
    counter = 0

    for file in filePath:
        with open(file, "r") as md_file:
            md_content = md_file.read()
        yaml_search = re.search('\-\-\-\\n(.*)\\n\-\-\-', md_content)
        if yaml_search:
            current_file_with_yaml = {
                "file": file,
                "tags": yaml_search.group(1).replace("Tags: ", "").split(',')
            }
            filename = current_file_with_yaml['file']
            tags = current_file_with_yaml['tags']

            # Add string to tag
            for tag in tags:
                tempTag.append("{}{}{}".format("<string>", tag.strip(), "</string>"))
                tagCounter += 1

            # combine tags to string
            taglist = "".join(tempTag)

            os.system("xattr -w \'com.apple.metadata:_kMDItemUserTags\' \'<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><array>{0}</array></plist>\' \'{1}\'".format(taglist, filename))

            # Empty tempTag list
            tempTag = []
            counter += 1

    os.system("osascript -e \'display notification \"{} Tags von {} Notizen erzeugt\" with title \"Tagify\"\'".format(tagCounter, counter))

def main():
    args = parser.parse_args()
    filePath = glob.glob(args.p + "/**/*.md", recursive=True)
    tagFiles(filePath)

if __name__ == '__main__':
    main()
