# Part of this code is from stackoverflow

import glob, argparse, pathlib, contextlib
from PIL import Image

parser = argparse.ArgumentParser(
    description="An application that creates a animated image (GIF or WEPB) from a series of images."
    "The input extension that should be used are given by --in and the directory is --dir."
)

parser.add_argument(
    "-d",
    "--dir",
    type=pathlib.Path,
    required=True,
    help=f"Directory where the images to be modified are.",
)

parser.add_argument(
    "-in",
    "--input",
    type=str,
    default="jpg",
    help="Input extensions for the images. They will be sorted. Default is 'jpg'.",
)

parser.add_argument(
    "-o",
    "--out",
    type=str,
    default="WEBP",
    help=f"Output file type, default is WEPB.",
)

parser.add_argument(
    "-dur",
    "--duration",
    type=int,
    default=1000,
    help=f"Duration of the animation, in ms.",
)

args = parser.parse_args()

# use exit stack to automatically close opened images
with contextlib.ExitStack() as stack:
    # GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_ALWAYS
    # GifImagePlugin.LOADING_STRATEGY = (
    #     GifImagePlugin.LoadingStrategy.RGB_AFTER_DIFFERENT_PALETTE_ONLY
    # )
    # GifImagePlugin.LOADING_STRATEGY = GifImagePlugin.LoadingStrategy.RGB_AFTER_FIRST

    # lazily load images
    img_paths = sorted(pathlib.Path.glob(args.dir, f"*.{args.input}"))
    imgs = (stack.enter_context(Image.open(f)) for f in img_paths)
    # extract  first image from iterator
    img = next(imgs)

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img.save(
        fp=args.dir / f"out.{args.out.lower()}",
        format=args.out,
        append_images=imgs,
        save_all=True,
        duration=args.duration // len(img_paths),
        loop=0,  # loop forever
    )
