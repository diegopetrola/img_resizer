import os, glob, pathlib, argparse
from PIL import Image


parser = argparse.ArgumentParser(
    description="This program modifies all image file extensions given by --in"
    " and saves them as the file extension given in --out."
)

parser.add_argument(
    "-in",
    "--input",
    type=str,
    nargs="+",
    required=True,
    help="Input extensions that will be modified. Multiple extensions can be given separated by spaces.",
)

parser.add_argument(
    "-out",
    "--output",
    required=True,
    type=str,
    help="Output extensions that will be saved.",
)

parser.add_argument(
    "-o",
    "--output_dir",
    help=f"Sets the output folder, if this is not set, the inpurt --dir will be used.",
)

parser.add_argument(
    "-d",
    "--dir",
    type=pathlib.Path,
    required=True,
    help=f"Directory where the images to be modified are.",
)

parser.add_argument(
    "-R",
    "--recursive",
    action="store_false",
    help=f"Also resizes images in subfolders of --dir",
)

args = parser.parse_args()
args.output_dir = args.output_dir or args.dir

if args.dir:
    for extension in args.input:
        x = pathlib.Path.glob(
            args.dir,
            pattern=f"**\*.{extension}" if args.recursive else f"*.{extension}",
        )
        for i in x:
            img = Image.open(i)
            name = i.name.replace(extension, args.output)
            img.save(i.parent / name)
            print(i.parent)
