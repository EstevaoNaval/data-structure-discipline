#include <stdlib.h>
#include <stdio.h>

typedef struct lista_encadeada{
    int informacao; // Aqui, pode-se armazenar qualquer dado relevante
    TLSE* next; // A pointer to list's next node
}TLSE;

TLSE * TLSE_removal(TLSE *l, int elem) {
    TLSE *p_ant = NULL, *p = l;

    while(p && p->informacao != elem) {
        p_ant = p;
        p = p->next;
    }

    if(!p) return l;

    if(!p_ant) l = l->next;
    else p_ant->next = p->next;

    free(p);

    return l;
}

TLSE * TLSE_removal_recursive(TLSE *l, int elem) {
    if(!l) return l;

    if(l->informacao == elem) {
        TLSE *p = l;
        l = l->next;
        free(p);
    }

    l->next = TLSE_removal_recursive(l->next, elem);
    return l;
}