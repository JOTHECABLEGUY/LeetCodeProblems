#include <stdc++.h>
using namespace std;
class KthLargest
{
public:
    priority_queue<int, vector<int>, greater<int>> heap;
    KthLargest(int k, vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        heap = slice(nums, k);
    }

    int add(int val)
    {
        int curr_kth = heap[0];
        if (val < curr_kth)
        {
            return curr_kth;
        }
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */