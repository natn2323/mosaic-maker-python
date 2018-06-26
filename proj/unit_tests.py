from sampler import euclidean_dist
from math import sqrt

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

