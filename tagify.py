import glob
import re
import os
import argparse

parser = argparse.ArgumentParser(description='Parse YAML Front Matters and write according OSX file tags.')
parser.add_argument('-p', '-path', type=str,
                    help='Path to folder which contains markdown files.')


class Stats(object):
    
    def __init__(self):
        self.tag_counter = 0
        self.file_counter = 0

    def increase_tag_counter(self):
        self.tag_counter += 1

    def increase_file_counter(self):
        self.file_counter += 1

    def increase_tag_counter_by(self, amount):
        self.tag_counter += amount

    def display_statistics(self):
        """
        Display statistics as osx notification
        """
        os.system("osascript -e \'display notification \"{} Tags von {} Notizen erzeugt\" with title \"Tagify\"\'".format(self.tag_counter, self.file_counter))


class Tagger(object):

    def __init__(self, stats):
        self.stats = stats

    def wrap_as_xml(self, tags):
        """
        Wrap tags in xml
        """
        return "".join(["<string>{}</string>".format(tag.strip()) for tag in tags])

    @staticmethod
    def append_xml_tags(xml_tags, filename):
        """
        Write wrapped xml tags to a file
        """
        os.system(
            "xattr -w 'com.apple.metadata:_kMDItemUserTags' " +
            "\"<!DOCTYPE plist PUBLIC '-//Apple//DTD PLIST 1.0//EN'" +
            "'http://www.apple.com/DTDs/PropertyList-1.0.dtd'>" +
            "<plist version='1.0'><array>{0}</array></plist>\" \'{1}\'".format(xml_tags, filename))

    def tag_files(self, file_path):
        """
        Read front matter tags in each file in file path
        """
        for file in file_path:
            with open(file, "r") as md_file:
                md_content = md_file.read()
            yaml_search = re.search('^---\n(.*)\n---', md_content)
            if yaml_search:
                yaml_front_matter = {
                    "file": file,
                    "tags": yaml_search.group(1).replace("Tags: ", "").replace("'", "").split(',')
                }
                xml_tags = self.wrap_as_xml(yaml_front_matter['tags'])
                self.append_xml_tags(xml_tags, yaml_front_matter['file'])
                self.stats.increase_tag_counter_by(len(yaml_front_matter['tags']))
                self.stats.increase_file_counter()

        self.stats.display_statistics()


def main():
    tagger = Tagger(Stats())
    args = parser.parse_args()
    filepath = glob.glob(args.p + "/**/*.md", recursive=True)
    tagger.tag_files(filepath)


if __name__ == '__main__':
    main()
