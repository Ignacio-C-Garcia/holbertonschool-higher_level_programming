#include "hash_tables.h"
hash_table_t *hash_table_create(unsigned long int size)
{
    hash_table_t *ht = malloc(sizeof(hash_table_t))
    if (!ht)
        return NULL;
    ht->size = size;
    ht->array = malloc(size * sizeof(hash_node_t *))
    if (!(ht->array))
        return NULL
    return  ht   
}