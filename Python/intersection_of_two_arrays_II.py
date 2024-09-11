"""350. Intersection of Two Arrays II
Easy
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?"""

import pytest
from typing import Dict, List, Union
from collections import Counter, defaultdict

class Solution:
    
    def test(self):
        return self.intersect_with_sorting([1, 2, 3, 4, 5, 6, 3], [2, 3, 4, 3])
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
            Find the intersection of two integer lists, including duplicates.

            This method returns a list of integers that appear in both input lists, 
            taking into account the number of occurrences of each integer. The result 
            will include each integer as many times as it appears in both lists.

            Args:
                nums1 (List[int]): The first list of integers.
                nums2 (List[int]): The second list of integers.

            Returns:
                List[int]: A list of integers that represent the intersection of the two lists, 
                including duplicates.
        """

        # result array to store final product
        res = []
        
        # create counters for both lists to allow for constant time lookup
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        # for each unique value in the first list, get the counts from each list. If there are any occurrences
        #   of the number in both lists, append the number to the result list the minimum number of times it appears in
        #   both lists 
        for num in set(nums1):
            count = min(c1.get(num, 0), c2.get(num, 0))
            if count > 0:
                res.extend([num]*count)
        
        # return the list
        return res
    
    def read_file_in_chunks(self, file:str, chunk_size:int):
        """
            Read a file in chunks and yield its contents as lists of strings.

            This generator function reads a specified file in chunks of a given size, 
            yielding each chunk as a list of strings split by commas. It allows for 
            efficient processing of large files without loading the entire file into memory.

            Args:
                file (str): The path to the file to be read.
                chunk_size (int): The size of each chunk to read from the file.

            Yields:
                List[str]: A list of strings representing the contents of each chunk, 
                split by commas.
        """

        # open the file and read in a chunk of the given size, the yield each chunk as a list of strings as needed
        with open(file, 'r') as f:
            while (chunk := f.read(chunk_size)):
                yield chunk.split(',')
                
    def build_counter(self, nums:Union[str, List[int]], mem_limit:int) -> Dict[int, int]:
        """
            Build a frequency counter for a list of integers or a file containing integers.

            This method creates a dictionary that counts the occurrences of each integer 
            in the provided list or in a file. If a string representing a file path is 
            given, it reads the file in chunks to manage memory usage efficiently.

            Args:
                nums (Union[str, List[int]]): A list of integers or a string representing 
                the path to a file containing integers.
                mem_limit (int): The maximum size of each chunk to read from the file.

            Returns:
                Dict[int, int]: A dictionary where the keys are integers and the values 
                are their respective counts.
        """
        
        # create a frequency dictionary over the given list
        counter = defaultdict(int)
        
        # if a file is given, process in chunks
        if isinstance(nums, str):
            for chunk in self.read_file_in_chunks(nums, mem_limit):
                
                # for each number from the file, if the string is empty, break as the chunk end has been reached, 
                #   otherwise update the count in the dictionary
                for num in chunk:
                    if num == '':
                        break
                    counter[int(num)] += 1
                    
        # if a list of numbers was given, get the counts of each number by iterating through the list 
        else:
            for num in nums:
                counter[num] += 1
        
        # return the frequency dictionary
        return counter
    
    def intersect_with_limited_memory(self, nums1:Union[str, List[int]], nums2:Union[str, List[int]], mem_limit:int) -> List[int]:
        """
            Find the intersection of two lists or files with limited memory usage.

            This method computes the intersection of two lists of integers or files 
            containing integers, while managing memory efficiently by using counters. 
            It returns a list of integers that appear in both inputs, including duplicates.

            Args:
                nums1 (Union[str, List[int]]): The first list of integers or a string 
                    representing the path to a file containing integers.
                nums2 (Union[str, List[int]]): The second list of integers or a string 
                    representing the path to a file containing integers.
                mem_limit (int): The maximum size of each chunk to read from the files.

            Returns:
                List[int]: A list of integers representing the intersection of the two 
                inputs, including duplicates.
        """
        
        # create the frequency dictionaries for both lists from the input lists or files
        counters = (self.build_counter(nums1, mem_limit), self.build_counter(nums2, mem_limit))
        
        # list to store output
        res = []
        
        # index within tuple of the smallest number of elements to process
        index = 0 if len(counters[0]) < len(counters[1]) else 1
        
        # for each entry in the smaller dictionary, check that the minimum frequency
        #   across both lists is above 0. If it is, add the number of shared occurrences 
        #   of the current number to the end of the result list
        for num, count in counters[index].items():
            if (c:=min(count, counters[index-1][num])) > 0:
                res.extend([num]*c)
        
        # return the output list
        return res
    
    def intersect_with_sorting(self, nums1:List[int], nums2:List[int]) -> List[int]:
        """
            Find the intersection of two sorted lists of integers.

            This method computes the intersection of two lists by first sorting them 
            and then using a two-pointer technique to identify common elements. 
            It returns a list of integers that appear in both input lists, including duplicates.

            Args:
                nums1 (List[int]): The first list of integers.
                nums2 (List[int]): The second list of integers.

            Returns:
                List[int]: A list of integers representing the intersection of the two 
                input lists, including duplicates.
        """
        
        # if any input list is empty, the intersection will also be empty
        if not nums1 or not nums2:
            return []
        
        # output list
        res = []
        
        # sort both input lists
        nums1.sort()
        nums2.sort()
        
        # initialize pointers to the current position in each list
        num1_pointer, num2_pointer = 0, 0
        
        # while teh indices do not go out of bounds
        while num1_pointer < len(nums1) and num2_pointer < len(nums2):
            
            # if a None element was found, return as any comparison will yield an error
            if nums1[num1_pointer] is None or nums2[num2_pointer] is None:
                return res
            
            # if the value from the first list is greater than the value from the second list,
            #   increment the second list's position as this will increase the chance of a common element being found
            if nums1[num1_pointer] > nums2[num2_pointer]:
                num2_pointer += 1
            
            # if the value from the first list is below the value from the second list, increment
            #   the first list's position for the reason mentioned above
            elif nums1[num1_pointer] < nums2[num2_pointer]:
                num1_pointer += 1
            
            # when a common element is found, add to the output list since this means an intersection was found.
            #   increment the first and second lists' positions to avoid repeating operations
            else:
                res.append(nums1[num1_pointer])
                num1_pointer += 1
                num2_pointer += 1
        
        # return the completed intersection list
        return res

@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        # Happy path tests
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
        ([1, 2, 3], [4, 5, 6], []),
        
        # Edge cases
        ([], [], []),
        ([1, 2, 3], [], []),
        ([], [1, 2, 3], []),
        ([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]),
        ([1, 2, 3], [3, 2, 1], [1, 2, 3]),
        
        # Error cases
        ([1, 2, 3], [None], []),
        ([None], [1, 2, 3], []),
    ],
    ids=[
        "happy_path_1",
        "happy_path_2",
        "happy_path_3",
        "edge_case_empty_lists",
        "edge_case_nums2_empty",
        "edge_case_nums1_empty",
        "edge_case_all_duplicates",
        "edge_case_all_elements_intersect",
        "error_case_nums2_contains_none",
        "error_case_nums1_contains_none",
    ]
)
def test_intersect(nums1, nums2, expected):
    # Act
    result = Solution().intersect_with_sorting(nums1, nums2)

    # Assert
    assert sorted(result) == sorted(expected)

if __name__ == "__main__":
    print(Solution().test())