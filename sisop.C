#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

pthread_mutex_t lock;

void* thread_function(void* arg) {
    pthread_mutex_lock(&lock);
    printf("Thread %ld telah memasuki bagian kritis.\n", (long) arg);
    // Bagian kritis: Hanya satu thread yang dapat menjalankan ini pada satu waktu
    sleep(1);  // Simulasi beberapa pekerjaan
    printf("Thread %ld meninggalkan bagian kritis.\n", (long) arg);
    pthread_mutex_unlock(&lock);
    return NULL;
}

int main() {
    pthread_t t1, t2;
    pthread_mutex_init(&lock, NULL);

    pthread_create(&t1, NULL, thread_function, (void*)1);
    pthread_create(&t2, NULL, thread_function, (void*)2);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    pthread_mutex_destroy(&lock);
    return 0;
}
