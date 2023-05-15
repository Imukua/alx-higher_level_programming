#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
    int i, j, len = 0;
    int arr[10000];
    listint_t *current;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    current = *head;

    while (current != NULL)
    {
        arr[len] = current->n;
        current = current->next;
        len++;
    }

    for (i = 0, j = len - 1; i <= j; i++, j--)
    {
        if (arr[i] != arr[j])
            return (0);
    }

    return (1);
}

