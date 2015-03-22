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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
    	ListNode *dummy = new ListNode(0);
    	dummy -> next = head;
    	ListNode *p = dummy,*q,*r;
    	for(int i = 1;i <= m-1;i++)
    	{
    		p = p->next;
    	}
    	ListNode *temp = p,*nh = p->next;
    	p = p->next;
    	q = p;
    	if(q == NULL)
    	{
    		return head;
    	}
    	r = p->next;
    	for(int i = m;i <= n-1;i++)
    	{
    		
    		q = r;
    		r = r->next;
    		q->next = p;
    		p = q;
    	}
        temp->next = q;
        nh ->next = r;
        return dummy->next;
    }
};