# README #

Tagify reads the YAML Front Matters of your markdown files and creates according OS X tags.

## Installation

```bash
pip3 install tagify
```

## Usage

Files that you want to be tagged need to have this pattern at the beginning:

```
---
Tags: foo, bar, baz
---
```

Use command line interface to specify path from where to search markdown files:

```bash
tagify -p your/path
```

## Contributing

Contributions are always welcome. Please feel free to fork this project and 
contact us if your changes should go upstream.

## Authors
- Simon Breiter
- Emanuele Mazzotta
