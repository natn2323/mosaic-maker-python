def easy_create(filename, color=(0,0,0)):
    img = Image.new("RGB", (360, 360), color)
    img.save(filename)

if __name__ == '__main__':
    import sys

    from PIL import Image
    
    print("Input your colors:")
    r = raw_input("Red: ")
    g = raw_input("Green: ")
    b = raw_input("Blue: ")
    color = (int(r), int(g), int(b))

    easy_create(sys.argv[1], color=color)

