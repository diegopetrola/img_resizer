# img_resizer
A script in python to resize all images in a folder.

## Installation and Requirements

`img_resizer` requires `python` and `pillow`.
Python should be installed on most operating systems by default and instructions to installing pillow can be seen (here)[https://pillow.readthedocs.io/en/stable/installation.html].

# Example Usage

To resize all images in the folder `C:\TestFolder\` to *70%* or their width type:

```
python img_resizer.py -d 'C:\TestFolder\' -W 0.7
```

The resized images will be found at `C:\TestFolder\output`


## Parameters

### `-d` or `--dir`
Directory where the images to be resized are

### `-H` or `--height`
Sets the new height for the images as a ratio (e.g. 0.5 = 50%). Images will keep their aspect ratio if only one of `-H` or `-W` is set.

### `-W` or `--height`
Sets the new width for the images as a ratio (e.g. 0.5 = 50%). Images will keep their aspect ratio if only one of `-H` or `-W` is set.

### `-R` or `---recursive`
Also resizes images in subfolders of `--dir`.

### `-o` or `--output_dir`
Sets the default output folder, this configuration will be saved for further uses.


