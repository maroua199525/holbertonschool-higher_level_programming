#include "lists.h"

/**
 * is_palindrome - check the list is palindrome
 * @head: pointer of pointer to list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	size_t i = 0, j = 0;
	listint_t *tmp;
	int array[1024];

	if (*head == NULL)
	{
		return (1);
	}
	tmp = *head;
	while (tmp != NULL)
	{
		array[i] = tmp->n;
		i++;
		tmp = tmp->next;
	}
	if (i == 0)
	{
		return (1);
	}
	while (j < (i / 2))
	{
		if (array[j] != array[i - 1 - j])
			return (0);
		j++;
	}
	return (1);
}
