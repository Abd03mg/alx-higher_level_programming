#include "lists.h"

/**
 * check_cycle - function that checks if there is cycle in linked list.
 *
 * @list: pointer to linked list.
 * Return: 0 if there is no cycle, 1 if there.
 */

int check_cycle(listint_t *list)
{
	void *add = list;

	while (list)
	{
		list = list->next;
		if (add == list)
			return (1);
	}
	return (0);
}


