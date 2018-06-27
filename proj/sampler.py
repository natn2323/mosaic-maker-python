"""
Assumptions:
- Reusing provided images (will eventually provide an option to enforce # of provided images == # of mosaic partitions)
- Sampling from full-sized photos and never from thumbnails

Features:
- ability to increase # of partitions
- ability to increase # of samples taken from larger image
- randomized sampling (will eventually make this optional)
- unit testing
- Euclidean distance to calculate image similarity
"""

#######################################BEGINNING#####################################
from math import sqrt
import os

def partition_and_calculate(filename, n):
    """
    Function prototype:
        partition_and_calculate(filename, n=3, max_subsamples=1)
    Function parameters (required):
        filename - the name of the image file
    Function parameters (optional):
        n - the number of partitions
        max_subsamples - the number of samples to take from each partition in determining the average color; 
                         the higher, the more accurate the average color of the image and the more samples to take
                         the lower, the less accurate the average color of the image but the fewer samples to take
    Return:
        storage - a list of tuples of RGB values; each tuple represents the average color of a partition
    """

    img = Image.open(filename)

    n = n # You'll get n*n partitions; n*n samples when subsamples=1
    max_subsamples = 1 # max_subsamples >= 1; 
                       # set max_subsamples to 1 if you want the same # of subsamples,
                       # set max_subsamples > 1 if you want random number of subsamplings;
                       # there should be n*n*subsamples number of subsamples

    width, height, temp = img.size[0], img.size[1], []
    storage = [[0 for x in range(n)] for y in range(n)]
    r_sum, g_sum, b_sum = 0, 0, 0

    val_error_flag, temp_count = False, None

    for i in range(0, n): # 0 (inclusive) to n (exclusive)
        x0, x1 = width*(i/float(n)), width*((i+1)/float(n))
        for j in range(0, n):
            y0, y1 = height*(j/float(n)), height*((j+1)/float(n))

            subsamples = random.randint(1, max_subsamples) # at least 1 subsample, at most max_subsamples
            for k in range(0, subsamples):
                rand_width = random.randint(int(x0), int(x1-1))
                print(y0, y1-1)
                print(int(y0), int(y1-1))
                rand_height = random.randint(int(y0), int(y1-1))
                temp.append(img.getpixel((rand_width, rand_height)))

                """
                try:
                    rand_width = random.randint(int(x0), int(x1-1))
                    rand_height = random.randint(int(y0), int(y1-1))
                    temp.append(img.getpixel((rand_width, rand_height)))
                except ValueError: # If you receive a ValueError, it means that partitions are very small, 
                                   # and for c in [x0,x1,y0,y1], c%1 == c, i.e. c is at the tenths/hundredths
                                   # level. This causes randint(1, 0) typically. Answer is to either decrease
                                   # number of partitions, or resize the original image so that it can be
                                   # partitioned so many times
                    print("y0, y1-1 == {}, {}".format(int(y0), int(y1-1)))
                    print("y0, y1-1 == {}, {}".format(y0, y1-1))
                    val_error_flag = True
                    temp = k
                finally:
                    if val_error_flag == True and temp_count is not None:
                        n = 
                """        
                

            # Calculate average color for the partition
            for rgb in temp:
                r_sum = r_sum + rgb[0]
                g_sum = g_sum + rgb[1]
                b_sum = b_sum + rgb[2]
            r_avg = r_sum / len(temp)
            g_avg = g_sum / len(temp)
            b_avg = b_sum / len(temp)
            storage[i][j] = (r_avg, g_avg, b_avg)
            
            r_sum, g_sum, b_sum, temp = 0, 0, 0, [] # resetting variables

    return storage 


def calculate_average(storage):
    """
    Function prototype:
        calculate_average(storage)
    Function parameters (required):
        storage - a list of tuples with RGB values; this list will be iterated and, using the values obtained,
                  will find the average RGB value
    Function parameters (optional):
        None
    Return:
        toRet - a tuple representing the average color for a given list of tuples of RGB values
    """
    # Calculate average color for all partitions, i.e. the image
    r_image, g_image, b_image = 0, 0, 0
    for row in storage:
        for col in row:
            r_image = r_image + col[0]
            g_image = g_image + col[1]
            b_image = b_image + col[2]

    r_image = r_image / len(storage)**2
    g_image = g_image / len(storage)**2
    b_image = b_image / len(storage)**2
    toRet = (r_image, g_image, b_image)

    #print("Average color of image is: ", toRet)
    #print("Let's create an image using the average color.")

    img = Image.new("RGB", (360, 360), toRet)
    img.save("average.jpg")

    #print("Done creating new image of the average color.")
    return toRet

def euclidean_dist(first, second):
    """
    Function prototype:
        dist(first, second)
    Function parameters (required):
        first - the first tuple of RGB values
        second - the second tuple of RGB values
    Function parameters (optional):
        None
    Return:
        The Euclidean distance between the first and second RGB tuples
    """
    return sqrt( (first[0] - second[0])**2 + (first[1] - second[1])**2 + (first[2] - second[2])**2 )

def dist_unit_test():
    """
    Just a unit test.
    """
    assert euclidean_dist((0,0,0), (0,0,0)) == 0
    assert euclidean_dist((0,0,0), (1,2,3)) == sqrt(14)
    assert euclidean_dist((-1,-1,-1), (0,0,0)) == sqrt(3)
    assert euclidean_dist((-1,-1,-1), (-1,-1,-1)) == 0
    assert euclidean_dist((-1,-1,-1), (1,1,1)) == sqrt(12)
    assert isinstance(euclidean_dist((0,0,0), (0,0,0)), float)
    assert isinstance(euclidean_dist((-1,-1,-1), (0,0,0)), float)

def calculate_similarity(original, match):
    """
    Function prototype:
        calculate_similarity(original, match)
    Args:
        original - the first list of tuples of RGB values to check from
        match - the second list of tuples of RGB values to check against the first list of tuples of RGB values
    Return:
        A float which represents the Euclidean distance
    """
    return euclidean_dist((original[0], original[1], original[2]), (match[0], match[1], match[2]))


def unit_test(storage):
    """
    Just a unit test.
    """

    if isinstance(storage, list):
        result = ""
        for each in storage:
            for i in range(0, 3):
                try:
                    assert 0 <= each[i] <= 256
                except AssertionError:
                    result = "Failed (AssertionError)"
                except Exception as e:
                    result = "Failed (General Error: {e})".format(e=str(e))
                else:
                    result = "Passed"
                finally:
                    output = "| {each}: Index {index}: {result} |".format(each=each, index=i, result=result) # Appending comma -> parentheses in output
                    print "{}".format(output) # Prints on new lines
            print ""

    elif isinstance(storage, tuple):
        result = ""
        for index, value in enumerate(storage):
            try:
                assert 0 <= value <= 256
            except AssertionError:
                result = "Failed (AssertionError)" 
            except Exception as e:
                result = "Failed (General Error: {e})".format(e=str(e))
            else:
                result = "Passed"
            finally:
                output = "| {value}: Index {index}: {result} |".format(value=value, index=index, result=result)
                print "{}".format(output)
        print ""

def setup(interactive_flag):
    setup_parameters = None
    if interactive_flag == False:
        return ('random.jpg', 100000, '/photos_to_choose_from/', 3)
    else:
        filename = raw_input("Please enter the filename of your mosaic image: ")
        while not os.path.isfile(filename):
            filename = raw_input("Please enter an existing filename within this directory: ")

        mosaic_n = raw_input("Please enter the number of partitions for your mosaic image: ")
        while not mosaic_n.isdigit() or mosaic_n <= 0:
            mosaic_n = raw_input("Please enter a valid number of partitions for the mosaic image: ")

        color_n = raw_input("Please enter the number of partitions for your comprising images: ")
        while not color_n.isdigit() or color_n <= 0:
            color_n = raw_input("Please enter a valid number of partitions for the comprising images: ")

        color_files_dir = raw_input("Please enter the name of the folder containing your comprising images: ")
        while not os.path.isdir(color_files_dir):
            color_files_dir = raw_input("Please enter an existing directory within this directory: ")

        return (filename, mosaic_n, color_files_dir, color_n)


if __name__ == "__main__":
    from PIL import Image
    from pprint import pprint
    import random, os, sys, math

    ####################################################### Find Computation Parameters ##########################################################
    interactive_flag = False
    """
    Interactive mode needs inputs for:
        -n
        -folder of comprising photos
        -file name of photo to turn into a mosaic
        -option to get comprising photos from web (Selenium)
        -interactive setting of n, in the case that the given n is invalid
    """

    # Finding the files from which the mosaic will be comprised
    color_n, color_list = 3, []
    files = os.listdir(os.getcwd() + '/photos_to_choose_from/')
    color_files = [os.path.abspath('./photos_to_choose_from/' + i) for i in files]

    # Finding the file for the mosaic
    mosaic = 'random.jpg'

    # Determining N - the number of partitions for the mosaic
    mosaic_n = 100000

    # Determining the given image's size
    mosaic_im = Image.open(mosaic)
    width, height = mosaic_im.size[0], mosaic_im.size[1]

    # For checking the thumbnail size; only to be used with -i interactive flag, otherwise we'll use default n, or decently low value of n
    mos_n = float(mosaic_n)
    while width/mos_n < 1 or height/mos_n < 1:
        #print("w,h is: {}, {}".format(width/mos_n, height/mos_n))
        lowest_n = None
        if width < height:
            lowest_n = width-1
        elif height < width:
            lowest_n = height-1

        print("Number of partitions must be within the range of [1, {}]. The second number is taken from the lesser of the width and height.".format(lowest_n))
        response = raw_input("Enter a new number of partitions: ")
        while True:
            if response.isdigit() and (1 <= int(response) <= lowest_n):
                mos_n = float(response)
                break
            else:
                response = raw_input("Please enter a valid number between 1 and {}: ".format(lowest_n))

    mosaic_n = int(math.floor(mos_n))
    thumbnail_size, thumbnail_list = (width/mosaic_n, height/mosaic_n), []



    ####################################################### Computations Done -- Begin Process ####################################################
    # Partitioning the image to become the mosaic
    mosaic_storage = partition_and_calculate(mosaic, mosaic_n)
    mosaic_final = []

    # Partitioning the images that will comprise the mosaic
    for colors in color_files:
        storage = partition_and_calculate(colors, color_n)
        final = calculate_average(storage)
        color_list.append(final)

    # Making the comprising images into thumbnails and normalizing their heights & widths
    for image in color_files:
        im = Image.open(image)
        im = im.resize(thumbnail_size)
        thumbnail_list.append(im)

    # Comparing the mosaic's partitions to the thumbnail partitions
    for row_index in range(len(mosaic_storage)):
        for col_index in range(len(mosaic_storage[row_index])):
            partition_rgb, comparison_dict = mosaic_storage[row_index][col_index], {}
            for index, color in enumerate(color_list):
                # Associating index of thumbnail to its similarity with partition
                comparison_dict[str(index)] = calculate_similarity(partition_rgb, color)

            # Finding thumbnail with highest (Euclidean distance) similarity to partition
            # TODO if you wanted to have unique comprising images, implement it here
            most_similar_index = None
            for key, value in sorted(comparison_dict.iteritems(), key=lambda (k,v): (v,k)):
                most_similar_index = int(key)             
                break

            # Saving index of thumbnail to paste into mosaic
            comparison_dict = {}
            mosaic_final.append(most_similar_index)

    # To have a whole image, new image size is based directly on thumbnail sizes, 
    # not mosaic image size
    new_im = Image.new("RGB", (thumbnail_size[0]*mosaic_n, thumbnail_size[1]*mosaic_n))
    new_im_width, new_im_height = new_im.size[0], new_im.size[1]

    # Pasting the thumbnail into [x][y] regions of mosaic
    count = 0
    try:
    #for k in range(0, len(mosaic_final)):
        for i in range(0, mosaic_n): # 0 (inclusive) to n (exclusive)
            x0, x1 = thumbnail_size[0]*i, thumbnail_size[0]*(i+1)
            for j in range(0, mosaic_n):
                y0, y1 = thumbnail_size[1]*j, thumbnail_size[1]*(j+1)
                if j%5 == 0:
                    #print('\n')
                    pass
                paste_box = (x0, y0, x1, y1)
                new_im.paste(thumbnail_list[mosaic_final[count]], paste_box)

                count = count + 1
    except ValueError:
        print("error thrown on: {}".format(thumbnail_list[mosaic_final[count]]))
        print("paste box on er: {}".format(paste_box))

    new_im.save('pixelated.jpg')
    new_im.show()

    """
    When you have partitioned lists of the large image and all the smaller ones, you should create a mapping between the smaller and the larger ones, i.e.
    {"larger_partition_1": ["match_1", "match_2", "match_3"], "larger_partition_2": ["match_1", "match_2", "match_3"], ... }
    The number of matches should be configurable.
    There should be a threshold/defined cutoff value for when the Euclidean distance is too different to be considered a match, 
    or have a ranking (e.g. only consider the top 20). 
    Perhaps, have something like, if "large_image.rgb - 10 < smaller_image_to_match.rgb < large_image.rgb + 10", then consider it a match
    """
    from unit_tests import dist_unit_test
    from unit_tests import unit_test
    dist_unit_test()
    
