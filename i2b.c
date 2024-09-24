#include <stdio.h>
#define N 32

int main(int argc, char *argv[]) {
  int n = 12345;
  int binRep[N];
  int i;

  for (i = 0; i < N; i++) {
    binRep[i] = 0;
  }

  i = 0;
  while (n > 0) {
    binRep[i] = n % 2;
    n = n / 2;
    i++;
  }
 
  for (i = N - 1; i >= 0; i--) {
    printf("%d", binRep[i]);
  }
  printf("\n");
  return 0;
}
