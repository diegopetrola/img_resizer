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
    action="store_true",
    help=f"Also resizes images in subfolders of --dir",
)

parser.add_argument(
    "-D",
    "--delete",
    action="store_true",
    help=f"Delete the original files (the original files will be lost!)",
)


args = parser.parse_args()
args.output_dir = args.output_dir or args.dir
print(args.delete, args.recursive)

print(args.input)

if args.dir:
    for extension in args.input:
        p = f"**/*.{extension}" if args.recursive else f"*.{extension}"
        print(p)
        x = pathlib.Path.glob(
            args.dir,
            pattern=p,
        )
        for i in x:
            print(i)
            img = Image.open(i)
            name = i.name.replace(extension, args.output)
            img.save(i.parent / name)
            if args.delete:
                os.remove(i)
