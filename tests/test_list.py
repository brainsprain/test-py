from nose.tools import assert_equal


class TestList():
    def test_slice_append(self):
        x = [1, 2, 3, 4]
        x[len(x):] = [5, 6, 7]
        assert_equal(x,[1,2,3,4,5,6,7])

