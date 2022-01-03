#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: header of a linked list
* Return: 1 if it is a palindrome 0 otherwise
*/
int is_palindrome(listint_t **head)
{
	int *buffer = NULL;
	listint_t *aux = *head;
	int counter = 0;
	int i = 0;

	if (aux && aux->next != NULL)
	{
		while (aux)
		{
			counter++;
			aux = aux->next;
		}

		buffer = malloc(counter * sizeof(int));

		while (*head)
		{
			buffer[i] = aux->n;
			i++;
			*head = (*head)->next;
		}
		counter--;

		for (i = 0; i < counter; i++)
		{
			if (buffer[i] != buffer[counter])
			{	free(buffer);
				return (0);
			}
			counter--;
		}
		free(buffer);
	}
	return (1);
}
