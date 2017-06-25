#include "list.h"

struct ListNode* swapPairs(struct ListNode* head) {
	if(head == NULL || head->next == NULL)
		return head;

	struct ListNode* pnewhead = head->next;
	head->next = pnewhead->next;
	pnewhead->next = head;
	//while(pnewhead->next->next)   why this fucking shit will lead to error dead circle?  
	//because always return newhead,like 1->2->3, 2->1->3->null,  always return 3, so it is a dead circle damn!
	//why add this while judgement ? why? fuck!   waste a lot of time
	pnewhead->next->next = swapPairs(pnewhead->next->next);
	return pnewhead;
}

void main()
{
	struct ListNode a = {
		.val = 1,
		.next = NULL,
	};

	struct ListNode b = {
		.val = 2,
		.next = NULL,
	};

	struct ListNode c = {
		.val = 3,
		.next = NULL,
	};
	a.next = &b;
	//b.next = &c;
	printf("%p\n",&a);
	swapPairs(&a);

}
