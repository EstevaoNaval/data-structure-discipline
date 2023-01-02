#include "TList.h"

TList * create_list(void) { 
    return NULL;
}

TList * search_list(TList *list, int info) {
    TList *list_pointer = list; // set a point with list's first node
    for (; list_pointer != NULL; list_pointer = list_pointer->next) { // Go through the list searching for passed information
        if(list_pointer->info == info) return list_pointer; // if found information, return the node with passed information
    }

    return list_pointer;
}

TList * search_list_recursive(TList * list, int info) {
    if(!list || list->info == info) return list; // if node information is equal to passed information, return this node
    return search_list_recursive(list->next, info); // pointer to list's next node
}

TList * remove_list(TList *l, int elem) {
    TList *p_ant = NULL, *p = l;

    while(p && p->info != elem) {
        p_ant = p;
        p = p->next;
    }

    if(!p) return l;

    if(!p_ant) l = l->next;
    else p_ant->next = p->next;

    free(p);

    return l;
}

TList * remove_list_recursive(TList *l, int elem) {
    if(!l) return l;

    if(l->info == elem) {
        TList *p = l;
        l = l->next;
        free(p);
    }

    l->next = TLSE_removal_recursive(l->next, elem);
    return l;
}

TList * insert_list(TList *list, int info) {
    TList *new_node = (TList*)malloc(sizeof(TList)); // Allocate a piece of principal memory to be linked list's new node
    new_node->info = info; // insert information in new node
    new_node->next = list; // New node next pointer points to list's first node 
    return new_node; // Return a new list wich begin with a new node
}

TList * insert_list_recursive(TList *list, int info) {
    if(list->next == NULL) { // if list pointer to NULL, insert a new node in list  and return tha new list
        return insert_list(list, info);
    }

    list->next = insert_list_recursive(list->next, info); // insert a new list ending with a new node
    return list; // return new list
}

TList * sorted_inserction_recursive(TList * list, int info) {
    // if node's information number is greater than num info passed, return a list list beginning with new node wich pointing to
    // node with greater num info
    if(list->next == NULL || list->info >= info) return insert_list(list, info);
    
    list->next = sorted_inserction_recursive(list->next, info);
    return list;
}

void print_list(TList *l) {
    TList *p = l;
    while(p) {
        printf("%d\n", p->info);
        p = p->next;
    }
}

void print_list_recursive(TList *l) {
    TList *p = l;
    while (p)
    {
        printf("%d\n", p->info);
        print_list_recursive(p->next);
    }
}

void print_reverse_recursive(TList *l) {
    TList *p = l;
    while (p)
    {
        print_reverse_recursive(p->next);
        printf("%d\n", p->info);
    }
}