resizePixel
==========================

[![Build Status](https://travis-ci.org/mtchavez/python-package-boilerplate.png?branch=master)](https://travis-ci.org/mtchavez/python-package-boilerplate)
[![Requires.io](https://requires.io/github/mtchavez/python-package-boilerplate/requirements.svg?branch=master)](https://requires.io/github/mtchavez/python-package-boilerplate/requirements?branch=master)

change quality of the image

## Package

Basic structure of package is

```
.
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── resizePixel
│   ├── __init__.py
│   ├── resizePixel.py
│   └── version.py
├── script
│   └── test
├── setup.py
└── tests
    ├── __init__.py
    ├── __pycache__
    │   └── __init__.cpython-39.pyc
    ├── img
    │   └── test.png
    └── unit
        ├── __init__.py
        ├── test_resizePixel.py
        └── test_version.py
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

    Start the tests


## Usage

<code>

    # import library 

    from resizePixel.resizePixel import rpImage,reduce_qualtiy
    from PIL import Image
    import os
    # image path
    image_path = r"C:\Users\mkshgh\Downloads\img.png"
    # I am saving in the same directory 
    # img_path,img_name > C:\Users\mkshgh\Downloads, img.png
    img_path,img_name = os.path.split(image_path)
    output_img_name = 'output_'+img_name

    # open the image and check the current quality
    image_file = Image.open(image_path)
    my_image = rpImage(image_path,image_file)
    info = my_image.get_image_meta()
    print(info)

    # decrease quality explained above
    # Use quality from 1 to 99; 99 being the best and 1 being the worst quality
    # If the quality of the image is already low use 1 to 20; works great with larger files.
    new_image = reduce_qualtiy(output_img_name,image_file,quality=50,outputdir=img_path)
    print(new_image)
</code>
