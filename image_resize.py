from PIL import Image
import argparse
import os
import sys
import glob


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Image resize program')
    parser.add_argument('-i', '--input_file',
                        metavar='<path_to_file>',
                        dest='input_path',
                        required=True,
                        help='full path to the image which '
                             'you need to transform')
    parser.add_argument('--width',
                        metavar='N',
                        dest='width',
                        required=False,
                        help='width of output image (pix)')
    parser.add_argument('--height',
                        metavar='N',
                        dest='height',
                        required=False,
                        help='height of output image (pix)')
    parser.add_argument('--scale',
                        metavar='N',
                        dest='scale',
                        required=False,
                        default=1,
                        help='scale of output image (from 0)')
    parser.add_argument('-o', '--output_directory',
                        metavar='<output_directory>',
                        dest='output_directory',
                        required=False,
                        help='path to output file directory')
    parser.conflict_handler = check_parser_arguments(parser)
    return parser.parse_args()


def check_parser_arguments(parser):
    args = parser.parse_args()
    if args.input_path and not os.path.isfile(args.input_path):
        raise parser.error('Input path is not a file')
    if args.scale and int(args.scale) < 0:
        raise parser.error('Scale must be positive')
    if args.scale and (args.width or args.height):
        raise parser.error('You should not specify width or '
                           'height with scale together')
    if args.output_directory and not(os.path.isdir(args.output_directory)):
        raise parser.error('Wrong path to output directory')
    # if args.width and args.height:
    #     return 'WARN: The proportions may not coincide with the original image'


def get_image(path_to_image):
    image = Image.open(path_to_image)
    return image


def get_new_size(image_width, image_height, parser):
    args = parser.parse_args()
    if args.width and not (args.height or args.scale):
        new_width = args.width
        new_height = args.height * new_width / image_width
        new_sizes = new_width, new_height
        return new_sizes


def resize_image(path_to_original, path_to_result):
    pass
    #img = get_image(path_to_original)
    file_name, file_ext = os.path.splitext(path_to_original)
    original_widht, original_heght = img.size
    #new_img_size = int(args.width), int(args.height)
    new_img = img.resize(new_img_size)
    # new_img.save(path_to_result + file_name + '__' + args.width + 'x' +args.height + file_ext)


if __name__ == '__main__':
    args = get_arguments()
    if check_parser_arguments(args):
            sys.exit(check_parser_arguments(args))
    image = get_image(args.path_to_image)
    image_width, image_height = image.sizes
    new_size = get_new_size(image_width, image_height, args)
    print(new_size)
    # if args.output_directory:
    #     path_to_result = args.output_directory
    # else:
    #     path_to_result = ''
    # if os.path.isfile(args.input_path):
    #     path_to_original = args.input_path
    #     resize_image(path_to_original, path_to_result)
    # else:
    #     print('File does not exist')
