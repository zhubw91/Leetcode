/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 // Merge Sort for Linked List
class Solution {
public:
	ListNode *listsplit(ListNode *head)
	{
		if(head == NULL || head->next == NULL)
		{
			return head;
		}
		ListNode *r = head, *p = head->next, *q = head->next;
		while(q != NULL)
		{
			q = q->next;
			if(q != NULL)
			{
				q = q->next;
				p = p->next;
				r = r->next;
			}		
		}
		r->next = NULL;
		return p;
	}
	ListNode *merge(ListNode *A, ListNode *B)
	{
		if(A == NULL)
		{
			return B;
		}
		if(B == NULL)
		{
			return A;
		}
		ListNode *r = A, *p = A->next, *q = B, *t;
		if(A->val > B->val)
		{
			t = q->next;
			q->next = A;
			A = q;
			r = A;
			p = A->next;
			q = t;
		}
		while(p != NULL && q != NULL)
		{
			if(p->val <= q->val)
			{
				p = p->next;
				r = r->next;
			}
			else
			{
				t = q->next;
				q->next = p;
				r->next = q;
				r = q;
				q = t;
			}
		}
		if(q != NULL)
		{
			r->next = q;
		}
		return A;
	}
    ListNode *sortList(ListNode *head)
    {
        if(head == NULL || head->next == NULL)
        {
        	return head;
        }
        else
        {
        	ListNode *b = listsplit(head);
        	ListNode *a = head;
        	a = sortList(a);
        	b = sortList(b);
        	return merge(a, b);
        }
    }
};