/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *removeNthFromEnd(ListNode *head, int n) 
    {
    	ListNode *p = head, *q = head, *r = NULL;
    	if(head == NULL || head->next == NULL) return NULL;
    	while(n > 0)
    	{
    		p = p->next;
    		n--;
    	}
    	while(p != NULL)
    	{
    		r = q;
    		q = q->next;
    		p = p->next;
    	}
    	if(r == NULL)
    	{
    		head = head->next;
    	}
    	else
    	{
    		r->next = q->next;    		
    	}
    	return head;
        
    }
};