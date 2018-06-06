from PIL import Image
import argparse
import os
import glob


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
                        dest='output_path',
                        required=False,
                        help='path to output file directory')
    return parser.parse_args()
    # print(args.accumulate(args.integers))


if __name__ == '__main__':
    args = get_arguments()
    if os.path.isfile(args.input_path):
        img = get_image(args.input_path)
        file_name, file_ext = os.path.splitext(args.input_path)
        img_size = img.size
        if args.width and args.height:
            new_img_size = int(args.width), int(args.height)
            new_img = img.resize(new_img_size)
            new_img.save(file_name + '__' + args.width + 'x' +
                         args.height + file_ext)
    else:
        print('File does not exist')
