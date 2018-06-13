from PIL import Image
import argparse
import os
import sys
import glob


def generate_parser():
    parser = argparse.ArgumentParser(
        description='Image resize program')
    parser.add_argument('-I', '--input_file',
                        type=str,
                        metavar='<path_to_file>',
                        dest='input_path',
                        required=True,
                        help='full path to the image which '
                             'you need to transform')
    parser.add_argument('-W', '--width',
                        type=int,
                        metavar='N',
                        dest='width',
                        required=False,
                        help='width of output image (pix)')
    parser.add_argument('-H', '--height',
                        type=int,
                        metavar='N',
                        dest='height',
                        required=False,
                        help='height of output image (pix)')
    parser.add_argument('-S', '--scale',
                        type=float,
                        metavar='N',
                        dest='scale',
                        required=False,
                        help='scale of output image (from 0)')
    parser.add_argument('-O', '--output_directory',
                        type=str,
                        default='',
                        metavar='<output_directory>',
                        dest='output_directory',
                        required=False,
                        help='path to output file directory')
    return parser


def check_parser_arguments(input_path, width, height, scale,
                           output_directory, parser):
    if input_path and not os.path.isfile(input_path):
        parser.error('Input path is not a file')
    if scale and int(scale) < 0:
        parser.error('Scale must be positive')
    if scale and (width or height):
        parser.error('You should not specify width or height with '
                     'scale together')
    if output_directory and not(os.path.isdir(output_directory)):
        parser.error('Wrong path to output directory')


def get_image(path_to_image):
    return Image.open(path_to_image)


def get_new_size(image, args):
    image_width, image_height = image.size
    if args.width and not(args.height) and not (args.scale):
        new_width = int(args.width)
        new_height = int(image_height * args.width / image_width)
        return new_width, new_height
    elif args.height and not(args.width) and not(args.scale):
        new_height = int(args.height)
        new_width = int(image_width * args.height / image_height)
        return new_width, new_height
    elif args.scale and not(args.width) and not(args.height):
        new_width = int(image_width * args.scale)
        new_height = int(image_height * args.scale)
        return new_width, new_height
    elif args.width and args.height and not(args.scale):
        new_width = int(args.width)
        new_height = int(args.height)
        print('warn: The proportions may not coincide with the original image')
        return new_width, new_height
    else:
        return image_width, image_height


def resize_image(image, new_sizes):
    return image.resize(new_sizes)


def save_resized_image(image_path, resized_image, resized_image_folder,
                       width, height):
    file_name, file_ext = os.path.splitext(image_path)
    resized_image.save(resized_image_folder + file_name + '__' +
                       str(width) + 'x' + str(height) + file_ext)


if __name__ == '__main__':
    parser = generate_parser()
    args = parser.parse_args()
    check_parser_arguments(args.input_path, args.width, args.height,
                           args.scale, args.output_directory, parser)
    img = get_image(args.input_path)
    new_sizes = get_new_size(img, args)
    new_width, new_height = new_sizes
    new_img = resize_image(img, new_sizes)
    save_resized_image(args.input_path, new_img, args.output_directory,
                       new_width, new_height)
