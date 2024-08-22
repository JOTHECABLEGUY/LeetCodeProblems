#include <stdlib.h>
#include <iostream>
#include <queue>
using namespace std;
class KthLargest
{
private:
	priority_queue<int, vector<int>, greater<int>> heap;
	int k;
public:
	KthLargest(int k, vector<int> &nums)
	{
		this->k = k;
		for (int i : nums) {
			add(i);
		}
	}

	int add(int val)
	{	
		if (heap.size() < k || val > heap.top()) {
			heap.push(val);
		}
		if (heap.size() > k) {
			heap.pop();
		}
		return heap.top();
	}
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */

int main() { 
	vector<vector<int, vector<int>>, char*> test_case_1 = { 3, {3,21,3,4},  "add", "add", "add", "add" };

	//KthLargest* obj = new KthLargest(k, nums);
	//*int param_1 = obj->add(val);
	return 0; 
}