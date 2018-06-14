from PIL import Image
import argparse
import os


def generate_parser():
    parser = argparse.ArgumentParser(
        description='Image resize program')
    parser.add_argument(
        '-I',
        '--input_file',
        type=str,
        metavar='<path_to_file>',
        dest='input_path',
        required=True,
        help='full path to the image which you need to transform')
    parser.add_argument(
        '-W',
        '--width',
        type=int,
        metavar='N',
        dest='width',
        required=False,
        help='width of output image (pix)')
    parser.add_argument(
        '-H',
        '--height',
        type=int,
        metavar='N',
        dest='height',
        required=False,
        help='height of output image (pix)')
    parser.add_argument(
        '-S',
        '--scale',
        type=float,
        metavar='N',
        dest='scale',
        required=False,
        help='scale of output image (from 0)')
    parser.add_argument(
        '-O',
        '--output_directory',
        type=str,
        default='',
        metavar='<output_directory>',
        dest='output_directory',
        required=False,
        help='path to output file directory')
    return parser


def check_parser_arguments(
        input_path,
        width,
        height,
        scale,
        output_directory,
        parser):
    if input_path and not os.path.isfile(input_path):
        parser.error('Input path is not a file')
    if not(width or height or scale):
        parser.error('You forgot to specify at least one resize parameter')
    if (
            (width and width <= 0) or
            (height and height <= 0) or
            (scale and scale <= 0)
    ):
        parser.error('Size parametrs must be positive')
    if scale and (width or height):
        parser.error('You should not specify width or height with '
                     'scale together')
    if output_directory and not(os.path.isdir(output_directory)):
        parser.error('Wrong path to output directory')


def get_image(path_to_image):
    return Image.open(path_to_image)


def get_new_size(
        image_width,
        image_height,
        new_width,
        new_height,
        scale):
    if new_width and new_height:
        return new_width, new_height
    elif scale:
        new_width = int(image_width * scale)
        new_height = int(image_height * scale)
        return new_width, new_height
    elif new_width:
        new_height = int(image_height * new_width / image_width)
        return new_width, new_height
    elif new_height:
        new_width = int(image_width * new_height / image_height)
        return new_width, new_height
    else:
        return image_width, image_height


def is_not_original_proportions(
        image_width,
        image_height,
        new_width,
        new_height):
    return image_width/new_width != image_height/new_height


def save_resized_image(
        original_image_name,
        resized_image,
        path_to_save):
    width, height = resized_image.size
    file_name, file_ext = os.path.splitext(original_image_name)
    resized_image_name = '{}__{}x{}{}'.format(file_name, width,
                                              height, file_ext)
    resized_image.save(os.path.join(path_to_save, resized_image_name))


if __name__ == '__main__':
    parser = generate_parser()
    args = parser.parse_args()
    check_parser_arguments(
        args.input_path,
        args.width,
        args.height,
        args.scale,
        args.output_directory,
        parser)
    img = get_image(args.input_path)
    original_width, original_height = img.size
    new_sizes = get_new_size(
        original_width,
        original_height,
        args.width,
        args.height,
        args.scale)
    new_width, new_height = new_sizes
    if args.width and args.height:
        if is_not_original_proportions(
                original_width,
                original_height,
                new_width,
                new_height):
            print('warn: The proportions may not '
                  'coincide with the original image')
    new_img = img.resize(new_sizes)
    if args.output_directory:
        path_to_save = args.output_directory
    else:
        path_to_save = os.path.dirname(args.input_path)
    original_image_name = os.path.basename(args.input_path)
    save_resized_image(
        original_image_name,
        new_img,
        path_to_save)
