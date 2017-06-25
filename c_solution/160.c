#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define bool int
#define true 1
#define false 0

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
	struct ListNode *pa=headA,*pb=headB;
	int lengthA=0,lengthB=0;
	while(pa) {
		pa=pa->next;lengthA++;}
	while(pb) {
		pb=pb->next;lengthB++;}
	if(lengthA<=lengthB){

		int n=lengthB-lengthA;
		pa=headA;pb=headB;
		while(n) {
			pb=pb->next;n--;}
	}else{

		int n=lengthA-lengthB;
		pa=headA;pb=headB;
		while(n) {
			pa=pa->next;n--;}
	}
	while(pa!=pb){

		pa=pa->next;
		pb=pb->next;
	}
	return pa;
}
