#include <iostream>
#include <pthread.h>

using namespace std;

#define NUM_THREADS 5

void *PrintHello(void *threadid){

long tid;
tid=(long)threadid;
cout<<"Hello World! Thread ID, " <<tid<<endl;

pthread_exit(NULL);






}

int main(){

pthread_t threads[NUM_THREADS];
int rc;

int i;

for(i=0; i<NUM_THREADS;i++){

rc = pthread_create(&threads[i], NULL, PrintHello, (void *)i);


}
cout<<"Hello World!"<<endl;

return 0;

}







