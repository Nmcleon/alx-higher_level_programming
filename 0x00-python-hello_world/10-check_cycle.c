#include "lists.h"

/**
 * c_cycle - checks linked list for cycle
 * @list: list to check
 *
 * Return: 1 (SUCCESS) 0 (FAIL)
 */
int c_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
