# SEO Optimizer

Search engine optimization is a headache for every website at the beginning, especially with Baidu as the most used search engine in China (after all, Baidu is indeed a very good advertising company), unless you pay to place your website as an advertisement, or you have an amazing number of visitors to your website. Instead, we may need to choose to create clicks and hits manually.

## Prerequisites

- Python 3.12 or higher
- Git (optional, for cloning the repository)
- Google Chrome (latest version)

## Installation

Consider use `uv` install this project.

## Usage

Create a python project and run it:

```python
from seooptimizer.main import run

def main(keyword, loop=False):
    while True:
        if run(keyword, wait=5.5, turn_wait=2, depth=3) and not loop:
            break

if __name__ == "__main__":
    main("Keywords", loop=True)
```

Replace `Keywords` with your keywords.

## Copyright

Copyright © 2011-present Noctisynth, org. All rights reserved.

This project is released under Apache-2.0 License.
