#include "lists.h"

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int is_palindrome(struct ListNode** head) {
    struct ListNode* slow = *head;
    struct ListNode* fast = *head;
    struct ListNode* prev = NULL;
    struct ListNode* next = NULL;
    
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }
    
    if (fast != NULL) {
        slow = slow->next;
    }
    
    while (slow != NULL) {
        if (slow->val != prev->val) {
            return 0;
        }
        slow = slow->next;
        prev = prev->next;
    }
    
    return 1;
}

