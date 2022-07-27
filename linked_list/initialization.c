#include <stdlib.h>
#include <stdio.h>

typedef struct lista_encadeada{
    int informacao; // Aqui, pode-se armazenar qualquer dado relevante
    TLSE* prox; // Um ponteiro para o próximo nó da lista
}TLSE;

TLSE * TLSE_inicializa(void) {
    return NULL; // Configura a lista com o primeiro ponteiro apontando para nulo
}