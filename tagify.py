import glob
import re
import subprocess
import sys

DEBUG = True

files = glob.glob('/Users/simonbreiter/Documents/Notizen/Mathematik/*.md')

file_with_yaml = []

for file in files:
    with open(file, "r") as md_file:
        md_content = md_file.read()
    yaml_search = re.search('\-\-\-\\n(.*)\\n\-\-\-', md_content)
    if yaml_search:
        file_with_yaml.append({"file": file, "tags": yaml_search.group(1).replace("Tags: ", "").split(",")})

def write_attributes(F, TagList):
    Result = ""

    plistFront = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><array>'
    plistEnd = '</array></plist>'
    plistTagString = ''
    for Tag in TagList:
        plistTagString = plistTagString + '<string>{}</string>'.format(Tag.replace("'", "-"))
    TagText = plistFront + plistTagString + plistEnd

    OptionalTag = "com.apple.metadata:"
    XattrList = ["kMDItemFinderComment", "_kMDItemUserTags", "kMDItemOMUserTags"]
    for Field in XattrList:
        XattrCommand = 'xattr -w {0} \'{1}\' "{2}"'.format(OptionalTag + Field, TagText.encode("utf8"), F)
        if DEBUG:
            sys.stderr.write("XATTR: {}\n".format(XattrCommand))
        ProcString = subprocess.check_output(XattrCommand, stderr=subprocess.STDOUT, shell=True)
        Result += ProcString
    return Result


for file_to_tag in file_with_yaml:
    write_attributes(file_to_tag["file"], file_to_tag["tags"])
