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
    ListNode *partition(ListNode *head, int x) 
    {
        ListNode *headA = NULL, *headB = NULL, *pA = NULL, *pB = NULL;
        if(head == NULL)
        {
        	return NULL;
        }
        while(head != NULL)
        {
        	if(head->val < x)
        	{
        		if(headA == NULL)
        		{
        			headA = head;
        			pA = head;
        		}
        		else
        		{
        			pA->next = head;
        			pA = head;
        		}
        	}
        	else
        	{
        		if(headB == NULL)
        		{
        			headB = head;
        			pB = head;
        		}
        		else
        		{
        			pB->next = head;
        			pB = head;
        		}
        	}
        	head = head->next;
        }
        if(pB != NULL)
        {
        	pB->next = NULL;
        }
        if(headA == NULL)
        {
        	return headB;
        }
        else
        {
        	if(headB != NULL)
        	{
        		pA->next = headB;       	
        	}
        	return headA;        	
        }
    }
};