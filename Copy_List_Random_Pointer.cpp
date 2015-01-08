/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
 /*
 Basic idea: let each node in the copy list l2 first insert before the coressponding node in original list l1
 then set the random pointer then split the l2 from l1
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) 
    {
    	RandomListNode *l1 = head, *t = NULL, *l2;
    	if(head == NULL)
    	{
    		return NULL;
    	}
    	while(l1 != NULL)
    	{
    		t = l1 -> next;
    		RandomListNode *p = new RandomListNode(l1->label);
    		p -> next = t;
    		l1 -> next = p;
    		l1 = t;
    	}
    	l1 = head;
    	while(l1 != NULL)
    	{
    		if(l1->random != NULL) l1 -> next -> random = l1 -> random -> next;
    		l1 = l1 -> next -> next;
    	}
    	l1 = head;
    	l2 = head -> next;    
    	RandomListNode *head2 = l2;
    	while(l2 != NULL)
    	{
    		l1 -> next = l2 -> next;
    		if(l2 -> next != NULL)
    		{
				l2 -> next = l2 -> next -> next;
    		}
    		l1 = l1 -> next;
    		l2 = l2 -> next;
    		
    	}
    	return head2;

    }
};