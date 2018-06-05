from PIL import Image
import argparse
import os


def get_image(path_to_image):
    image = Image.open(path_to_image)
    return image


def resize_image(path_to_original, path_to_result):
    pass


def get_arguments():
    parser = argparse.ArgumentParser(
        description='Image resize program')
    parser.add_argument('-i', '--input_file',
                        metavar='<path_to_file>',
                        dest='path',
                        required=True,
                        help='full path to the image which '
                             'you need to transform')
    parser.add_argument('--width',
                        metavar='N',
                        required=False,
                        help='width of output image (pix)')
    parser.add_argument('--height',
                        metavar='N',
                        required=False,
                        help='height of output image (pix)')
    parser.add_argument('--scale',
                        metavar='N',
                        required=False,
                        help='scale of output image (from 0)')
    parser.add_argument('-o', '--output_directory',
                        metavar='<output_directory>',
                        help='path to output file directory')
    return parser.parse_args()
    # print(args.accumulate(args.integers))


if __name__ == '__main__':
    args = get_arguments()
    get_image(args.path)


