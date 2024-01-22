#include "lists.h"

/**
 * check_cycle - function that checks if its a cycle list.
 * @list: list to check
 * Return: 1 if there is a cycle or 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *new;

	tmp = new = list;

	while(tmp != NULL && new != NULL && new->next !=NULL)
	{
		new = new->next->next;
		tmp = tmp->next;
		if (new == tmp)
			return (1);
	}
	return (0);
}