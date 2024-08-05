#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset
    
    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Takes 2 integer arguments and returns a tuple of size two
        containing the start and end index corresponding to the range of
        indexes to return in a list for those pagination parameters
        Args:
            page (int): page number to return (pages are 1-indexed)
            page_size (int): number of items per page
        Return:
            tuple(start_index, end_index)
        """
        end = page * page_size
        start = end - page_size
        
        return (start, end)


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return a set of data

        Args:
            page (int): number of the page.Defaults to 1.
            page_size (int): size of the page. Defaults to 10.

        Returns:
            List[List]: all the rows from the page
        """
        assert isinstance(page, int) and page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "the page_size must be an integer greater than 0"
        
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        return dataset[start:end]

if __name__ == "__main__":
    server = Server()

    try:
        should_err = server.get_page(-10, 2)
    except AssertionError:
        print("AssertionError raised with negative values")

    try:
        should_err = server.get_page(0, 0)
    except AssertionError:
        print("AssertionError raised with 0")

    try:
        should_err = server.get_page(2, 'Bob')
    except AssertionError:
        print("AssertionError raised when page and/or page_size are not ints")


    print(server.get_page(1, 3))
    print(server.get_page(3, 2))
    print(server.get_page(3000, 100))