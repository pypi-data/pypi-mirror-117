# live-pandoc

live-pandoc is simple script designed to run a pandoc command against a file when changes to that file are detected.

## Installation

```sh
pip install live-pandoc
```

## Quickstart

live-pandoc was designed to be used identically to how pandoc would be used.

For example, if running the following pandoc command:

```sh
pandoc README.md -o README.pdf
```

The live-pandoc command would run as:

```sh
live-pandoc README.md -o README.pdf
```

When changes are detected in `README.md`, `pandoc README.md -o README.pdf` will be run.
