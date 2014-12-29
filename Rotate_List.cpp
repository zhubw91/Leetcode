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
    ListNode *rotateRight(ListNode *head, int k) 
    {
    	int length = 0;
    	ListNode *p = head, *tail = NULL, *q = NULL, *r = NULL;
    	if(p == NULL || p->next == NULL)
    	{
    		return p;
    	}
    	while(p != NULL)
    	{
    		length ++;
    		tail = p;
    		p = p->next;
    	}    
    	p = head;
    	q = head;
    	if(k >= length)
    	{
    		k = k%length;
    	}
    	while(k < length)
    	{
    		q = p;
    		p = p->next;
    		k++;
    	}
    	q->next = NULL;
    	if(p == NULL)
    	{
    		return head;
    	}
    	else
    	{
    		tail->next = head;
    		return p;
    	}
    }
};