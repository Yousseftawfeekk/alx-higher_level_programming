#include "lists.h"

/**
 * check_cycle - check if list is cyclical or not
 * @list: pointer to list to check
 * 
 * Return: 1 if cyclical, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
