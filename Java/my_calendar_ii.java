/*731. My Calendar II
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
At most 1000 calls will be made to book. */
import java.util.*;
class MyCalendarTwo {

    // lists to hold both the single booked and the double booked intervals
    ArrayList<int[]> single_bookings;
    ArrayList<int[]> double_bookings;
    
    public MyCalendarTwo() {
        this.single_bookings = new ArrayList<>();
        this.double_bookings = new ArrayList<>();
    }
    
    /**
     * Method to book a specified interval while considering past booked intervals. If a booking would cause a triple
     *  booking, return false, otherwise book the interval and return true
     * @param start (int): start time of the interval to book
     * @param end (int): end time of the interval to book
     * @return boolean: whether the given interval can be booked without causing a triple booking
     */
    public boolean book(int start, int end) {

        // exit early if inputs are invalid
        if (end < start || start < 0 || end < 0) return false;

        // check the double bookings first, return false if there is overlap with the current interval and any double booked sessions
        for (int[] p : this.double_bookings) if (end > p[0] && start < p[1]) return false;

        // pairs to add back into the single bookings
        int[][] add_pairs = new int[2][2];

        // index of what to remove from the single bookings list
        int index = -1;
        for (int i = 0; i < this.single_bookings.size(); i++){

            // get the current index's start and end
            int s = this.single_bookings.get(i)[0];
            int e = this.single_bookings.get(i)[1];

            // if there is no overlap, continue
            if (start >= e || end <= s) continue;

            // get the overlap interval and add it to the double booking ist
            int[] overlap = new int[]{Math.max(start, s), Math.min(end, e)};
            this.double_bookings.add(overlap);

            // get the non-overlapping portions of the intersecting interval 
            int[] left = new int[]{Math.min(start, s), overlap[0]};
            int[] right = new int[]{overlap[1], Math.max(end, e)};

            // place the non-overlaps in the add_pairs array to add them back to the single bookings list
            add_pairs[0] = left;
            add_pairs[1] = right;

            // set the index of the interval to remove from the list
            index = i;
        }

        // if an overlap was found
        if (index > -1){

            // add the non-overlapping portions to the single bookings list
            for (int[] r : add_pairs) this.single_bookings.add(r);

            // remove the original interval
            this.single_bookings.remove(index);

            // if no overlap found, add the whole interval to the single booking list
        } else this.single_bookings.add(new int[]{start, end});

        // return true
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */
