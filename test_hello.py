from hello import toyou,add,substract

def setup_function(function):
    print("Running Setup: %s" % function.__name__)
    function.x = 10


def teardown_function(function):
    print("Running Teardown: %s" % function.__name__)
    del function.x


### Run to see failed test
def test_hello_add():
    assert add(test_hello_add.x) == 11


def test_hello_toyou():
    assert toyou(test_hello_toyou.x) == "hi abc"


def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
