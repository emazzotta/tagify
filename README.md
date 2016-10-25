# README #

Tagify reads the YAML Front Matters of your markdown files and creates according OS X tags.

## Installation

```bash
pip3 install tagify
```

## Usage

Files that you want to be tagged need to have this pattern at the beginning:

```md
---
Tags: foo, bar, baz
---
```

Use command line interface to specify path from where to search markdown files:

```bash
tagify -p your/path
```

## Authors
- Simon Breiter
- Emanuele Mazzotta
