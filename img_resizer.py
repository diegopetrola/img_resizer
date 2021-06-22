import os, glob, pathlib, argparse, json
from PIL import Image
from utils import utils

IMG_TYPES = ('*.jpg', '*.png', '*.tga', '*.tif', '*.dds')

# configs will be stored here
CONF_FILE = 'conf.json'

DEFAULT_CONF = {
    'output_dir': 'output'
}

with open(CONF_FILE, 'r') as file:
    s = file.read()
    if s == '':
        conf = DEFAULT_CONF
    else:
        conf = json.loads(s)

parser = argparse.ArgumentParser(
    description = "This program resizes all images in a given folder" \
        " and outputs them on another one (default: output, can be set with -o)."
)

parser.add_argument('-H', '--height', 
                    help= 'Sets the new height. Images will keep their aspect \
                        ratio if only one of -H or -W is set.')

parser.add_argument('-W', '--width', type=float,
                    help= 'Sets the new width. Images will keep their aspect \
                        ratio if only one of -H or -W is set.')

parser.add_argument('-o', '--output_dir',
                    help= f'Set the default output folder, this config will be saved for further uses')

parser.add_argument('-d', '--dir', type=pathlib.Path,
                    help= f'Directory where the images to be resized are')

parser.add_argument('-R', '--recursive', action='store_true',
                    help= f'Also resizes images in subfolders of --dir')

parser.add_argument('-c', '--cap', type=int,
                    help= f'If, after resized, the image is still below --cap value, \
                        it will capped to --cap.')

args = parser.parse_args()
args.output_dir = args.output_dir or conf["output_dir"]
args.dir = os.path.abspath(args.dir)

if args.dir:
    if args.recursive:
        path = os.path.join (args.dir, '**')
        print(path)
    else:
        path = args.dir
    print(f"path: {path}")
    for extension in IMG_TYPES:
        path = os.path.join (path, extension)
        globpath = glob.glob( path )
        print(globpath)
        for file in glob.glob( path, recursive=True ):
            with Image.open(file) as img:
                path1, filename = os.path.split(file)
                size = img.size
                size = utils.calculate_new_size(size, args.width)
                new_img = img.resize(size)
                path = os.path.join(args.dir, args.output_dir)
                if os.path.isdir(path):
                    path = os.path.join(path, filename)
                else:
                    os.mkdir(path)
                    path = os.path.join(path, filename)

                # new_img.save(path)
                print(f"{utils.bcolors.OKGREEN}Saved file{utils.bcolors.ENDC}: {path}")

if args.output_dir and args.output_dir != conf['output_dir']:
    with open(CONF_FILE, 'w+') as file:
        conf['output_dir'] = args.output_dir
        json.dump(conf, file, indent=4)
