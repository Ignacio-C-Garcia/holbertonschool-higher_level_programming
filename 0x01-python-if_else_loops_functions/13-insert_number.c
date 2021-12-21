#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *aux = *head;
	listint_t *node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;
	if (*head)
	{
		while((*head)->n < number && (*head)->next && (*head)->next->n < number)
		{
			*head = (*head)->next;
		}
		node->next = (*head)->next;
		(*head)->next = node;
		*head = aux;
		return (node);
	}
	else
	{
		*head = node;
		return (node);
	}
}
