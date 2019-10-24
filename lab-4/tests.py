import unittest
from Tree import Tree, string_to_people


class TestTree(unittest.TestCase):
    def test_string_to_people(self):
        test_string = "YNYN YNNY YNNY NYYY NYNY NYYN"
        people = string_to_people(test_string)
        self.assertEqual([[1, 3], [1, 4], [1, 4], [2, 3, 4], [2, 4], [2, 3]], people)

    def test_counting_ways(self):
        input_string = "YNN YNY YNY NYY NYY NYN"
        people = string_to_people(input_string)
        tree = Tree()
        for person in people:
            tree.add_person(person)

        ways = tree.do_it()
        self.assertEqual(2, ways)

    def test_empty_ways(self):
        input_string = ""
        people = string_to_people(input_string)
        tree = Tree()
        for person in people:
            tree.add_person(person)

        ways = tree.do_it()
        self.assertEqual(0, ways)
