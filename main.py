from PIL import Image  # import library to work with images

ASCII_CHARS = "@%#*+=-:. "  # ASCII characters


def resize_image(image, new_width=100):  # function to resize image
    width, height = image.size  # get image width and height
    ratio = height / width  # calculate aspect ratio

    new_height = int(new_width * ratio * 0.55)  # calculate new height
    resized = image.resize((new_width, new_height))  # resize image

    return resized  # return resized image


def grayify(image):  # function to convert image to grayscale
    gray = image.convert("L")  # convert to grayscale (0–255 values)
    return gray  # return grayscale image


def pixels_to_ascii(image):  # function to convert pixels to ASCII
    pixels = image.getdata()  # get all pixels from image

    result = ""  # empty string for result

    for pixel in pixels:  # loop through each pixel
        index = pixel * (len(ASCII_CHARS) - 1) // 255  # get index based on brightness
        result += ASCII_CHARS[index]  # add character to result

    return result  # return ASCII string


def create_ascii_image(image, width=100):  # main function
    image = resize_image(image, width)  # resize image
    image = grayify(image)  # convert to grayscale

    ascii_str = pixels_to_ascii(image)  # convert pixels to ASCII

    ascii_image = ""  # empty string for final image

    for i in range(0, len(ascii_str), width):  # loop in steps of width
        line = ascii_str[i:i + width]  # get one line
        ascii_image += line + "\n"  # add line and new line

    return ascii_image  # return final ASCII image


img = Image.open("image.png")  # open image file

ascii_art = create_ascii_image(img, 100)  # create ASCII image

print(ascii_art)  # print result

file = open("ascii_image.txt", "w")  # open file for writing
file.write(ascii_art)  # write ASCII to file
file.close()  # close file