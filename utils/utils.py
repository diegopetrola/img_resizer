def calculate_new_size(size: tuple, factor:int, cap:int = float('inf')):
    pos = (0, 1) if size[0] > size[1] else (1, 0)
    aspect_ratio = size[pos[1]]/size[pos[0]]

    new_size = [0, 0]
    new_size[pos[0]] = int(min(size[pos[0]]*factor, cap))
    new_size[pos[1]] = int(new_size[pos[0]] * aspect_ratio )

    return new_size

# Piece of code from Blender
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
