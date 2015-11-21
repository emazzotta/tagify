# -*- coding: utf-8 -*-

import glob
import re
import os

files = glob.glob('/Users/simonbreiter/Documents/Notizen/Mathematik/*.md')

tempTag = []

for file in files:
    with open(file, "r") as md_file:
        md_content = md_file.read()
    yaml_search = re.search('\-\-\-\\n(.*)\\n\-\-\-', md_content)
    if yaml_search:
        current_file_with_yaml = {
            "file": file,
            "tags": yaml_search.group(1).replace("Tags: ", "").strip().replace(",","").split()
        }
        filename = current_file_with_yaml['file']
        tags = current_file_with_yaml['tags']

        # Add string to tag
        for tag in tags:
            tempTag.append("{}{}{}".format("<string>", tag, "</string>"))

        # combine tags to string
        taglist = "".join(tempTag)

        os.system("xattr -w \'com.apple.metadata:_kMDItemUserTags\' \'<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\"><array>{0}</array></plist>\' \'{1}\'".format(taglist, filename))

        # Empty tempTag list
        tempTag = []
