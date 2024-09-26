/*729. My Calendar I
Medium
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book. */

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */

import java.util.*;

class MyCalendar {
    private ArrayList<Integer> starts;
    private ArrayList<Integer> ends;

    public MyCalendar() {
        this.starts = new ArrayList<>();
        this.ends = new ArrayList<>();
    }
    
    public boolean book(int start, int end) {
        int count = 0, sp = 0, ep = 0;

        while (sp < this.starts.size() && ep < this.ends.size()){
            if (count > 1) return false;
            if (start < this.ends.get(ep) && end > this.starts.get(sp)) return false;
            if (this.starts.get(sp) < this.ends.get(ep)){
                count++; sp++; 
            } 
            else {
                count--; ep++;}
        }
        this.starts.add(start);
        this.ends.add(end);
        Collections.sort(this.starts);
        Collections.sort(this.ends);
        return true;
    }

    public static void main(String[] args) {
        MyCalendar obj = new MyCalendar();
        // boolean r;
        int[][] inputs = new int[][]{{10, 20}, {15, 25}, {20, 30}};
        boolean[] res = new boolean[inputs.length];
        for (int i = 0; i < inputs.length; i++){
            res[i] = obj.book(inputs[i][0], inputs[i][1]);
        }
        System.out.println(Arrays.toString(res));
    }
}
