class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (target == nums[i] + nums[j])
                    return {j, i};  // conventionally smaller index first
            }
        }
        return {}; // no solution found
    }
};