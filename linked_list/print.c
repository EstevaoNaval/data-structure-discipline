#include <stdlib.h>
#include <stdio.h>

typedef struct lista_encadeada{
    int informacao; // Aqui, pode-se armazenar qualquer dado relevante
    TLSE* next; // A pointer to list's next node
}TLSE;

void TLSE_print(TLSE *l) {
    TLSE *p = l;
    while(p) {
        printf("%d\n", p->informacao);
        p = p->next;
    }
}

void TLSE_print_recursive(TLSE *l) {
    TLSE *p = l;
    while (p)
    {
        printf("%d\n", p->informacao);
        TLSE_print_recursive(p->next);
    }
}

void TLSE_print_reverse_recursive(TLSE *l) {
    TLSE *p = l;
    while (p)
    {
        TLSE_print_reverse_recursive(p->next);
        printf("%d\n", p->informacao);
    }
}