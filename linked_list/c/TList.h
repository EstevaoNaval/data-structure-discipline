#include <stdlib.h>
#include <stdio.h>

typedef struct linked_list_node{
    int info; // Symbolizes the information stored in a list node
    struct linked_list_node * next; // A pointer to next list node
}TList;

TList * create_list(void); // Initializes a list
void print_list(TList *l); // Print a list
void print_list_recursive(TList *l); // Print a list recursively
void print_reverse_recursive(TList *l); // Print a reverse list recursively 
TList * search_list(TList *list, int info); // Search an info in a list
TList * search_list_recursive(TList * list, int info); // Search an info in a list recursively 
TList * insert_list(TList *list, int info); // Inserts a list node 
TList * insert_list_recursive(TList *list, int info); // Inserts a list node recursively
TList * sorted_inserction_recursive(TList * list, int info); // Inserts a list node recursively and with a sort
TList * remove_list(TList *l, int elem); // Removes a list node
TList * remove_list_recursive(TList *l, int elem); // Removes a list node recursively