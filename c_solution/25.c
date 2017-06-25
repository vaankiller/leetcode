#include "array.h"

int vsearchInsert(int* nums, int start, int end, int target)
{
	printf("%d,%d\n", start, end);
	if(nums == NULL)
		return -1;

	if(target <= nums[start])
		return start;
	else if(target == nums[end])
		return end;
	else if(target > nums[end])
		return end + 1;
	else
	{
		if(target < nums[(end-start)/2 + start])
			return vsearchInsert(nums, start, start+(end-start)/2-1, target);
		else if(target == nums[(end-start)/2 + start])
			return (end-start)/2+start; 
		else if(target > nums[(end-start)/2 + start])
			return vsearchInsert(nums, start+(end-start)/2+1, end, target);
	}
}

int searchInsert(int* nums, int numsSize, int target) 
{
	return  vsearchInsert(nums, 0, numsSize-1, target);
}

void main()
{
	int test[6] = {2,4,5,6,7,8};
	int t = 0;

	printf("%d\n", searchInsert(test, 6, 7));
}

/*
#include "list.h"

struct ListNode* reverseList(struct ListNode* head) {
	if(head == NULL || head->next == NULL)
		return head;

	struct ListNode* pre = NULL;
	struct ListNode* pcur = head;
	struct ListNode* next;

	while(pcur)
	{
		next = pcur->next;
		pcur->next = pre;
		pre = pcur;
		pcur = next;
	}
	return pre;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
	if(!head || !head->next || k <= 1)
		return head;

	struct ListNode *cur = head, *tail = head, *next, *newhead;
	int cnt = 1;

	for(cnt = 1; cur->next && cnt < k+1; cnt++)
		cur = cur->next;

	if(!cur->next && cnt != k)
		return head;
	else
	{
		next = cur->next;
		cur->next = NULL;

		newhead = reverseList(head);
		tail->next = reverseKGroup(next, k);
	}
	return newhead;    
}


void main()
{
	struct ListNode a = {
		.val = 2,
		.next = NULL,
	};

	struct ListNode b = {
		.val = 1,
		.next = &a,
	};

	reverseKGroup(&b, 2);
	return;
}
*/
