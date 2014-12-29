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
	ListNode* reverse(ListNode *head)
	{
		if(head == NULL || head->next == NULL)
		{
			return head;
		}
		ListNode *r = NULL, *p = head, *q = head->next;
		while(q != NULL)
		{
			p->next = r;
			r = p;
			p = q;
			q = q->next;
		}
		p->next = r;
		return p;
	}
	void merge(ListNode *A, ListNode *B)
	{
		ListNode *p = A, *q = B;
		while(q != NULL)
		{
			ListNode *t = q->next;
			q->next = p->next;
			p->next = q;
			p = q->next;
			q = t;
		}
	}
    void reorderList(ListNode *head) 
    {
        if(head != NULL && head->next != NULL)
        {
			ListNode *p = head, *q = head, *r = NULL;
			while(q != NULL)
			{
				r = p;
				p = p->next;
				q = q->next;
				if(q != NULL)
				{
					q = q->next;
				}
			}
			r->next = NULL;
			p = reverse(p);
			merge(head, p);

        }

    }
};