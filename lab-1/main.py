from read_from_file import read_from_file
from sorting_helicopters import sort_by_max_height, sort_by_max_mass
from copy import copy


list_of_helicopters = read_from_file("file.txt")

sort_by_max_height(copy(list_of_helicopters))  # Using copy so that original list isn't affected
sort_by_max_mass(copy(list_of_helicopters))