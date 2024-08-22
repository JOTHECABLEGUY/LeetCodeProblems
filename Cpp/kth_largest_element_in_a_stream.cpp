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
        for (int i : nums)
        {
            add(i);
        }
    }

    int add(int val)
    {
        if (heap.size() < k || val > heap.top())
        {
            heap.push(val);
        }
        if (heap.size() > k)
        {
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

int main()
{
    int k = 3;
    int kth_largest;
    vector<int> nums{3, 21, 3, 4};
    vector<string> commands{"add", "add", "add", "add"};
    vector<int> nums_to_add{6, 2, 5, 30};

    KthLargest obj(k, nums);
    for (const int i : nums_to_add)
    {
        kth_largest = obj.add(i);
        cout << kth_largest;
    }
    return 0;
}