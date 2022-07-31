#include <stdlib.h>
#include <stdio.h>

typedef struct lista_encadeada{
    int informacao; // Aqui, pode-se armazenar qualquer dado relevante
    TLSE* next; // A pointer to list's next node
}TLSE;

TLSE * TLSE_begin_inserction(TLSE *list, int info) {
    TLSE *new_node = (TLSE*)malloc(sizeof(TLSE)); // Allocate a piece of principal memory to be linked list's new node
    new_node->informacao = info; // insert information in new node
    new_node->next = list; // New node next pointer points to list's first node 
    return new_node; // Return a new list wich begin with a new node
}

TLSE * TLSE_end_inserction_recursive(TLSE *list, int info) {
    if(list->next == NULL) { // if list pointer to NULL, insert a new node in list  and return tha new list
        return TLSE_begin_inserction(list, info);
    }

    list->next =  TLSE_end_inserction_recursive(list->next, info); // insert a new list ending with a new node
    return list; // return new list
}

TLSE * TLSE_sorted_inserction_recursive(TLSE * list, int info) {
    // if node's information number is greater than num info passed, return a list list beginning with new node wich pointing to
    // node with greater num info
    if(list->next == NULL || list->informacao >= info) return TLSE_begin_inserction(list, info);
    
    list->next = TLSE_sorted_inserction_recursive(list->next, info);
    return list;
}
