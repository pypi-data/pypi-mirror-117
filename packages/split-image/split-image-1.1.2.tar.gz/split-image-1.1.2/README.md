# split-image


## Quickly split an image into rows and columns (tiles).

[split-image](https://pypi.org/project/split-image/) is a Python package that you can use from the command line to split an image into tile.

<p align="center">
<img width="75%" src="https://user-images.githubusercontent.com/9117427/130825947-e78c4d15-6a89-40f8-9aa1-ddfa3b23779c.png"/>
</p>

## Installation


`pip install split-image`

## Usage

From the command line:

`split-image [-h] [-s] image_path rows cols`

<p align="center">
<img width="75%" src="https://user-images.githubusercontent.com/9117427/130827013-1dfe300c-9a2d-4b44-a27b-86a6781e115b.png"/>
</p>

### Basic examples

`split-image cat.png 2 2`

This splits the `cat.png` image in 4 tiles (`2` rows and `2` columns).

<p align="center">
<img width="75%" src="https://user-images.githubusercontent.com/9117427/130825960-4db37eb7-08e0-467e-8f30-fcfd38cad732.png"/>
</p>

`split-image bridge.png 3 4 -s`

This splits the `bridge.png` image in 12 tiles (`3` rows and `4` columns). The `-square` arguments resizes the image into a square before splitting it. The background color used to fill the square is determined from the image automatically.

<p align="center">
<img width="75%" src="https://user-images.githubusercontent.com/9117427/130825967-f191a5d9-c5c6-4ee3-9dbe-5943a40725fd.png"/>
</p>


```

positional arguments:
  image_path    The path of the image to split.
  rows          How many rows to split the image into (horizontal split).
  cols          How many columns to split the image into (vertical split).

optional arguments:
  -h, --help    show this help message and exit
  -s, --square  If the image should be resized into a square before splitting.


```

