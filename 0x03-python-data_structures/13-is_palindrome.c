#include <stdio.h>
#include <stdlib.h>

/**
* struct Node - Structure for a node in a linked list
* @data: The data stored in the node
* @next: Pointer to the next node
*/
typedef struct Node
{
	int data;
	struct Node *next;
} Node;

/**
* is_palindrome - Checks if a singly linked list is a palindrome
* @head: Double pointer to the head of the linked list
*
* Return: 1 if the linked list is a palindrome, 0 otherwise
*/
int is_palindrome(Node **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	Node *slow = *head, *fast = *head, *prev = NULL, *temp;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow;
		slow = slow->next;
		temp->next = prev;
		prev = temp;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (prev->data != slow->data)
			return (0);

		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}

/**
* insert - Inserts a new node at the beginning of a linked list
* @head: Double pointer to the head of the linked list
* @data: The data to be inserted
*/
void insert(Node **head, int data)
{
	Node *new_node = malloc(sizeof(Node));
	if (new_node == NULL)
		exit(EXIT_FAILURE);

	new_node->data = data;
	new_node->next = *head;
	*head = new_node;
}

/**
* display - Displays the elements in a linked list
* @head: Pointer to the head of the linked list
*/
void display(Node *head)
{
	while (head)
	{
		printf("%d ", head->data);
		head = head->next;
	}
	printf("\n");
}

int main(void)
{
	Node *head = NULL;

	// Inserting elements into the linked list
	insert(&head, 1);
	insert(&head, 2);
	insert(&head, 3);
	insert(&head, 2);
	insert(&head, 1);

	printf("Linked list: ");
	display(head);

	if (is_palindrome(&head))
		printf("The linked list is a palindrome.\n");
	else
		printf("The linked list is not a palindrome.\n");

	return 0;
}

