#include "lists.h"
/**
*check_cycle - checks if a singly linked list has a cycle in it
*@list: listint_t
*Return: neither 0 or 1
*/
int check_cycle(listint_t *list)
{
	listint_t *ptr, *tmp;

	if (ptr == NULL || list == NULL)
	{
		return (0);
	}
	ptr = list;
	tmp = list->next;
	while (tmp != NULL)
	{
		if (ptr == tmp)
		{
			return (1);
		}
		ptr = ptr->next;
		tmp = tmp->next->next;
	}
	return (0);
}
