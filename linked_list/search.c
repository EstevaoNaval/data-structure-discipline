#include <stdlib.h>
#include <stdio.h>

typedef struct lista_encadeada{
    int informacao; // Aqui, pode-se armazenar qualquer dado relevante
    TLSE* next; // A pointer to list's next node
}TLSE;

TLSE * TLSE_search(TLSE *list, int info) {
    TLSE *list_pointer = list; // set a point with list's first node
    for (; list_pointer != NULL; list_pointer = list_pointer->next) { // Go through the list searching for passed information
        if(list_pointer->informacao == info) return list_pointer; // if found information, return the node with passed information
    }

    return list_pointer;
}

TLSE * TLSE_search_recursive(TLSE * list, int info) {
    if(!list || list->informacao == info) return list; // if node information is equal to passed information, return this node
    return TLSE_search_recursive(list->next, info); // pointer to list's next node
}