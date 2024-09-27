"""731. My Calendar II
Medium
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.


Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book."""

import pytest
class MyCalendarTwo:

    def __init__(self):
        self.single_bookings = []
        self.double_bookings = []

    def book(self, start: int, end: int) -> bool:
        """
            Schedule a new booking in the calendar and manage overlaps.

            This function attempts to book a time interval defined by the start and end times. It checks for 
            potential overlaps with existing bookings and ensures that no time slot is triple booked. If the 
            booking is successful, it updates the internal lists of single and double bookings accordingly.

            Args:
                start (int): The start time of the booking.
                end (int): The end time of the booking.

            Returns:
                bool: True if the booking was successful, False if the booking could not be made due to 
                    invalid inputs or overlaps that would cause triple bookings.
        """
        
        # exit early if inputs are invalid
        if start < 0 or end < 0 or end < start: return False
        
        # check for overlaps with double booked intervals, return False if a portion will be triple booked
        for p in self.double_bookings:
            if start < p[1] and end > p[0]: return False
            
        # pair to remove from the single list, pairs to add outside of the overlapping portion
        remove_pair, add_pairs = None, []
        for p in self.single_bookings:
            
            # if no overlap, move to next iteration
            if start >= p[1] or end <= p[0]: continue
            
            # get overlapping portion of the overlap
            double_pair = (max(start, p[0]), min(end, p[1]))
            
            # portion to the left and right of the overlap
            start_pair = (min(p[0], start), double_pair[0])
            end_pair = (double_pair[1], max(end, p[1]))
            
            # add the overlap to the double booking list
            self.double_bookings.append(double_pair)
            
            # add the non overlapping portions to the list of pairs to add back to the single bookings list
            add_pairs = [start_pair, end_pair]
            
            # the pair to remove from the single bookings list since an overlap was found
            remove_pair = p
        
        # remove the pair and add the non overlapping portions to/from the single bookings list
        if remove_pair: 
            self.single_bookings.remove(remove_pair)
            self.single_bookings.extend(add_pairs)
            
        # otherwise just add the whole input interval
        else: self.single_bookings.append((start, end))
        
        # return True
        return True

obj = MyCalendarTwo()
@pytest.mark.parametrize("start, end, expected", [
    (10, 20, True),  # happy path
    (15, 25, True),  # overlapping single booking
    (20, 30, True),  # adjacent booking
    (5, 10, True),   # non-overlapping booking
    (10, 40, False),  # large booking
    (25, 35, True),  # overlapping single booking
    (5, 15, True),   # overlapping single booking
    (10, 20, False), # double booking
    (15, 25, False), # double booking
    (20, 30, False), # double booking
    (0, 0, True),    # edge case: zero length booking
    (0, 1, True),    # edge case: minimal booking
    (1, 1, True),    # edge case: zero length booking
    (1, 2, True),    # edge case: minimal booking
    (10, 10, True),  # edge case: zero length booking
    (-10, 10, False),  # error case: negative start
    (10, -10, False),  # error case: negative end
    (20, 10, False),   # error case: end before start
], ids=[
    "happy_path_1", "happy_path_2", "happy_path_3", "happy_path_4", "happy_path_5",
    "happy_path_6", "happy_path_7", "double_booking_1", "double_booking_2", "double_booking_3",
    "edge_case_zero_length_1", "edge_case_minimal_1", "edge_case_zero_length_2", 
    "edge_case_minimal_2", "edge_case_zero_length_3", "error_case_negative_start", 
    "error_case_negative_end", "error_case_end_before_start"
])
def test_book(start, end, expected):
    
    # Act
    result = obj.book(start, end)

    # Assert
    assert result == expected

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)