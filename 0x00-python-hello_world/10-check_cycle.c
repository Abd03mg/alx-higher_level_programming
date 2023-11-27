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

	if (list == NULL || list->next == NULL)
		return (0);
	while (list && list->next && list->next->next)
	{
		list = list->next;
		if ((char *)add == (char *)list)
			return (1);
	}
	return (0);
}


