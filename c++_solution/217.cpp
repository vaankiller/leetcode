
class Solution {
	public:
		bool containsDuplicate(vector<int>& nums) {
			set<int> s;
			int len = nums.size();
			for(int i=0; i<len; i++)
			{
				if(s.find(nums[i]) == s.end())
					s.insert(nums[i]);
				else
					return true;
			}
			return false;
		}
};
