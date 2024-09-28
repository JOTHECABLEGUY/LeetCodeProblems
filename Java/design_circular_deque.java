/*641. Design Circular Deque
Medium
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.

Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull. */


class MyCircularDeque {
    private int size; 
    private int[] data;
    private int max_size;
    public MyCircularDeque(int k) {
        this.max_size = k;
        this.data = new int[k];
        for (int i = 0; i < k; i++){
            this.data[i] = -1;
        }
        this.size = 0;
    }
    
    public boolean insertFront(int value) {
        if (this.isFull()) return false;
        if (this.data[0] == -1) {this.data[0] = value; this.size++; return true;}
        int index = 0;
        for(int i = 0; i < this.max_size-2; i++){
            if (this.data[i] == -1){
                index = i;
                break;
            }
        }
        while(index > 0){
            this.data[index] = this.data[index-1];
            this.data[--index] = -1;
        }
        this.data[0] = value;
        this.size++;
        return true;
    }
    
    public boolean insertLast(int value) {
        if (this.isFull()) return false;
        int last_index = this.max_size-1;
        if (this.data[last_index] == -1) {
            this.data[last_index] = value; 
            this.size++; 
            return true;
        }
        int index = 0;
        for(int i = last_index; i > -1; i--){
            if (this.data[i] == -1){
                index = i;
                break;
            }
        }
        while(index < last_index){
            this.data[index] = this.data[++index];
            this.data[index] = -1;
        }
        this.data[last_index] = value;
        this.size++;
        return true;
    }
    
    public boolean deleteFront() {
        if (this.isEmpty()) return false;
        for (int index = 0; index < this.max_size; index++){
            if (this.data[index] != -1){
                this.data[index] = -1;
                this.size--;
                return true;
            }
        }
        return false;
    }
    
    public boolean deleteLast() {
        if(this.isEmpty()) return false;
        for(int i = this.max_size-1; i > -1; i--){
            if (this.data[i] != -1){
                this.data[i] = -1;
                this.size--;
                return true;
            }
        }
        return false;
    }
    
    public int getFront() {
        if (this.isEmpty()) return -1;
        for (int i = 0; i < this.max_size; i++){
            if (this.data[i] != -1) return this.data[i];
        }
        return -1;
    }
    
    public int getRear() {
        if (this.isEmpty()) return -1;
        for (int i = this.max_size-1; i > -1; i--){
            if (this.data[i] != -1) return this.data[i];
        }
        return -1;
    }
    
    public boolean isEmpty() {
        return this.size == 0;
    }
    
    public boolean isFull() {
        return this.size == this.max_size;
    }
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque obj = new MyCircularDeque(k);
 * boolean param_1 = obj.insertFront(value);
 * boolean param_2 = obj.insertLast(value);
 * boolean param_3 = obj.deleteFront();
 * boolean param_4 = obj.deleteLast();
 * int param_5 = obj.getFront();
 * int param_6 = obj.getRear();
 * boolean param_7 = obj.isEmpty();
 * boolean param_8 = obj.isFull();
 */