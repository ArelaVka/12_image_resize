from PIL import Image
import argparse
import os
import sys
import glob


def generate_parser():
    parser = argparse.ArgumentParser(
        description='Image resize program')
    parser.add_argument('-I', '--input_file',
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
                        type=int,
                        metavar='N',
                        dest='scale',
                        required=False,
                        help='scale of output image (from 0)')
    parser.add_argument('-O', '--output_directory',
                        metavar='<output_directory>',
                        dest='output_directory',
                        required=False,
                        help='path to output file directory')
    return parser


def check_parser_arguments(input_path, width, height, scale, output_directory, parser):
    if input_path and not os.path.isfile(input_path):
        parser.error('Input path is not a file')
    if scale and int(scale) < 0:
        parser.error('Scale must be positive')
    if scale and (width or height):
        parser.error('You should not specify width or height with scale together')
    if output_directory and not(os.path.isdir(output_directory)):
        parser.error('Wrong path to output directory')
    # if args.width and args.height:
    #     return 'WARN: The proportions may not coincide with the original image'


def get_image(path_to_image):
    return Image.open(path_to_image)


def get_new_size(image, args):
    image_width, image_height = image.size
    if args.width and not(args.height) and not (args.scale):
        new_width = args.width
        new_height = image_height * args.width / image_width
        return new_width, new_height
    elif args.height and not(args.width) and not(args.scale):
        new_height = args.height
        new_width = image_width * args.height / image_height
        return new_width, new_height
    elif args.scale and not(args.width) and not(args.height):
        new_width = image_width * args.scale
        new_height = image_height * args.scale
        return new_width, new_height
    elif args.width and args.height and not(args.scale):
        new_width = args.width
        new_height = args.height
        return new_width, new_height
    else:
        return image_width, image_height


def resize_image(args):
    file_name, file_ext = os.path.splitext(args.input_path)
    new_img_size = int(args.width), int(args.height)
    new_img = img.resize(new_img_size)
    # new_img.save(path_to_result + file_name + '__' + args.width + 'x' +args.height + file_ext)


if __name__ == '__main__':
    parser = generate_parser()
    args = parser.parse_args()
    check_parser_arguments(args.input_path, args.width, args.height, args.scale, args.output_directory, parser)
    img = get_image(args.input_path)
    new_sizes = get_new_size(img, args)
    print(new_sizes)

    # image = get_image(args.input_path)
    # image_width, image_height = image.size
    # new_size = get_new_size(image_width, image_height, args)
    # print(new_size)

    # if args.output_directory:
    #     path_to_result = args.output_directory
    # else:
    #     path_to_result = ''
    # if os.path.isfile(args.input_path):
    #     path_to_original = args.input_path
    #     resize_image(path_to_original, path_to_result)
    # else:
    #     print('File does not exist')
