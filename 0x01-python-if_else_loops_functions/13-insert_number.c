#include "lists.h"

/**
 * insert_node - the main function that insert
 * a number into a sorted singly linked list.
 * @head: a pointer to the head of linked list.
 * @number: the number to insert in new node.
 *
 * return: the adress of the new node, or NULL if it failed.
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == 0)
		return (0);
	new->n = number;

	if (node == 0 || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node->next != 0)
	{
		if ((node->next)->n >= number)
		{
			new->next = node->next;
			node->next = new;
			return (new);
		}
		node = node->next;
	}

	new->next = node->next;
	node->next = new;
	return (new);
}
