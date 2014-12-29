# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head == None:
        	return None
        p = head
        q = head.next
        while q != None:
        	if q.val >= p.val:
        		q = q.next
        		p = p.next
        	else:
        		r = head
        		t = head.next
        		if r.val > q.val:
        			p.next = q.next
        			q.next = r
        			head = q
        			q = p.next
        		else:
        			while t != q and t.val < q.val:
        				r = r.next
        				t = t.next
        			p.next = q.next
        			q.next = t
        			r.next = q
        			q = p.next

        return head
# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# class Solution {
# public:
#     ListNode *insertionSortList(ListNode *head) 
#     {
#         if (head == NULL)
#         {
#         	return NULL;
#         }
#         ListNode *p = head;
#         ListNode *q = head->next;
#         while(q != NULL)
#         {
#         	if (q->val >= p->val)
#         	{
#         		q = q->next;
#         		p = p->next;
#         	}
#         	else
#         	{
#         		ListNode *r = head;
#         		ListNode *t = head->next;
#         		if (r->val > q->val)
#         		{
#         			p->next = q->next;
#         			q->next = r;
#         			head = q;
#         			q = p->next;
#         		}
#         		else
#         		{
#         			while (t != q && t->val < q->val)
#         			{
#         				r = r->next;
#         				t = t->next;
#         			}
#         			p->next = q->next;
#         			q->next = t;
#         			r->next = q;
#         			q = p->next;
#         		}
#         	}
#         }
#         return head;   
#     }
# };

