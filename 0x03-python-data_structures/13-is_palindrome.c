#include "lists.h"
#include <stddef.h>
/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: header of a linked list
* Return: 1 if it is a palindrome 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	int buffer[1024];
	listint_t *aux = *head;
	int counter = 0;
	int i = 0;

	if (aux)
	{
		while (aux)
		{
			buffer[counter] = aux->n;
			counter++;
			aux = aux->next;
		}

		for (i = 0; i <= counter - 1; i++)
		{
			if (buffer[i] != buffer[counter - 1])
				return (0);
			counter--;
		}
	}
	return (1);
}
