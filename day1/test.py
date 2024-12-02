import os
import unittest
import part1
import part2


class TestSolution(unittest.TestCase):
    def test_create_lists(self):
        # Given
        test_list = [0, 1, 2, 3, 4, 5, 6, 7]

        # When
        list_1, list_2 = part2.create_lists(test_list)

        # Then
        self.assertListEqual(list_1, [0, 2, 4, 6])
        self.assertListEqual(list_2, [1, 3, 5, 7])

    def test_read_file(self):
        # Given
        file_path = os.path.join(os.path.dirname(__file__), "test_input")

        # When
        list = part2.read_file(file_path)

        # Then
        self.assertListEqual(list, [3, 4, 4, 3, 2, 5, 1, 3, 3, 9, 3, 3])

    def test_part_1(self):
        # Given
        file_path = os.path.join(os.path.dirname(__file__), "test_input")

        # When
        result = part1.main(file_path)

        # Then
        self.assertEqual(result, 11)

    def test_part_2(self):
        # Given
        file_path = os.path.join(os.path.dirname(__file__), "test_input")

        # When
        result = part2.main(file_path)

        # Then
        self.assertEqual(result, 31)


if __name__ == "__main__":
    unittest.main()
