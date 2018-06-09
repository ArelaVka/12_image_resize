from PIL import Image
import argparse
import os
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
    return parser


def check_parser_arguments(argument):
    if argument.scale and argument.scale < 0:
        argparse.error('ERROR: Scale must be positive')


def resize_image(path_to_original, path_to_result):
    img = get_image(path_to_original)
    file_name, file_ext = os.path.splitext(path_to_original)
    original_widht, original_heght = img.size
    new_img_size = int(args.width), int(args.height)
    new_img = img.resize(new_img_size)
    new_img.save(path_to_result + file_name + '__' + args.width + 'x' +args.height + file_ext)


def get_image(path_to_image):
    image = Image.open(path_to_image)
    return image


if __name__ == '__main__':
    args = get_arguments()
    check_parser_arguments(args)
    # if args.output_directory:
    #     path_to_result = args.output_directory
    # else:
    #     path_to_result = ''
    # if os.path.isfile(args.input_path):
    #     path_to_original = args.input_path
    #     resize_image(path_to_original, path_to_result)
    # else:
    #     print('File does not exist')
