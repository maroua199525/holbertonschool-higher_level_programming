#include "lists.h"
/**
*check_cycle - checks if a singly linked list has a cycle in it
*@list: listint_t
*Return: neither 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *head, *ptr;
	
	if (list == NULL)
		return (0);
	ptr = list;
	head = list->next;
	while (ptr && head && head->next)
	{
		if (ptr == head)
			return (1);
		ptr = ptr->next;
		head = head->next;
	}
	return (0);
}
