#include "lists.h"
#include <stddef.h>
int is_palindrome(listint_t **head)
{
	int buffer[1024];
	listint_t *aux = *head;
	int counter = 0;
	int i = 0;

	while(aux)
	{
		buffer[counter] = aux->n;
		counter++;
		aux = aux->next;
	}

	for(i = 0; i <= counter - 1; i++)
	{
		if(buffer[i] != buffer[counter - 1])
			return (0);
		counter--;
	}
	return (1);
}
