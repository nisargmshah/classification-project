from ImageConversion import Image
import sys


def main():
    name = "example.jpg"
    im64 = "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"
    #im64 = 2
    #im64 = "worthless"
    im = Image(input_image=im64, thefilename=name)
    im.encode_image_string()
    im.save_image_string(file="example_new.jpg")
    #imbin = Image(im.bin_from_64())
    #print(imbin.bin_from_64())
    print(im.print2())


if __name__ == "__main__":
    main() #sys.argv[1:])