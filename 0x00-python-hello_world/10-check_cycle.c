#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *A2 = list;
	listint_t *A1 = list;

	while (list)
	{
		if (A1->next)
			A1 = A1->next;
		if (A2->next)
		{
			A2 = A2->next;
			if (A2->next)
				A2 = A2->next;
			else
				return (0);
		}
		else
			return(0);
		if (A1 == A2)
			return (1);
	}
	return (0);
}
