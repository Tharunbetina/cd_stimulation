import unittest
from cd_stimulate import construct_new_path

# Assume the functions are imported from the module
# from mycd import normalize_path, is_valid_directory_name, construct_new_path


class TestCDCommand(unittest.TestCase):
    def test_cd_to_subdirectory(self):
        self.assertEqual(construct_new_path("/", "abc"), "/abc")

    def test_cd_to_subdirectory_in_path(self):
        self.assertEqual(construct_new_path("/abc/def", "ghi"), "/abc/def/ghi")

    def test_cd_to_parent_directory(self):
        self.assertEqual(construct_new_path("/abc/def", ".."), "/abc")

    def test_cd_to_absolute_path(self):
        self.assertEqual(construct_new_path("/abc/def", "/abc"), "/abc")

    def test_cd_to_deeper_absolute_path(self):
        self.assertEqual(construct_new_path("/abc/def", "/abc/klm"), "/abc/klm")

    def test_cd_to_multiple_parent_directories(self):
        self.assertEqual(construct_new_path("/abc/def", "../.."), "/")

    def test_cd_to_multiple_parent_directories_outside_root(self):
        self.assertEqual(construct_new_path("/abc/def", "../../.."), "/")

    def test_cd_to_current_directory(self):
        self.assertEqual(construct_new_path("/abc/def", "."), "/abc/def")

    def test_cd_to_invalid_directory_name(self):
        self.assertEqual(
            construct_new_path("/abc/def", "..klm"), "..klm: No such file or directory"
        )

    def test_cd_to_root_with_multiple_slashes(self):
        self.assertEqual(construct_new_path("/abc/def", "//////"), "/")

    def test_cd_to_invalid_path(self):
        self.assertEqual(
            construct_new_path("/abc/def", "......"),
            "......: No such file or directory",
        )

    def test_cd_to_complex_path(self):
        self.assertEqual(construct_new_path("/abc/def", "../gh///../klm/."), "/abc/klm")


if __name__ == "__main__":
    unittest.main()
