#include <stdio.h>
typedef int element;
int size, i = 0;

int partition (element a[], int begin, int end) {
    int pivot, L, R ,t;
    element temp;
    L = begin;
    R = end;
    pivot = (int)((begin+end)/2.0);

    printf("\n [%d단계 : pivot = %d] \n", ++i, a[pivot]);


    while ( L < R) {
        while((a[L] < a[pivot]) && (L<R))
            L++;
        while( (a[R] >= a[pivot]) && ( L < R))
            R--;
       if (L<R) {
            temp = a[L];
            a[L] = a[R];
            a[R] = temp;
       }
       if (L == pivot ) {
            pivot = R;
       }  // L이 피봇인 경우, 변경된 피봇 위치(R) 저장

    }  // While L < R loop


    temp = a[pivot];
    a[pivot] = a[R];
    a[R] = temp;
    // L = R이 된 경우, 더 이상이 진행 할 수 없으므로, 피봇원소와 R의 원소를 변경.
    //
    for ( t = 0; t < size; t++) {
        printf("%d ", a[t]);              
    }
    printf("\n");
    return R;
}

void quickSort(element a[], int begin, int end) {
    int p;
    if (begin < end ) {
          p = partition(a, begin, end); //피봇 위치에 의해 분할 위치를 결정
          quickSort(a, begin, p-1); // 피봇 왼쪽 부분 집합에 대해 퀵 정렬 재귀 호출
          quickSort(a, p+1,end); // 피봇 오른쪽 부분 집합에 대해 퀵 정렬 재귀 호출
    }

}

void main () {
    element list [8] = {69, 10, 30, 2, 16, 8, 31, 22};
    size = 8;
    printf("\n초기 상태");
    for ( int i = 0; i < size; i++){
        printf("%d ", list[i]);    

    }

    quickSort(list,0,size-1);

    getchar();
}
