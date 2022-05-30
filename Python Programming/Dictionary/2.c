#include <stdio.h>

int main(void) {
	int t,c,i,a1,a2,a3,a4,a5,a6,a7;
	scanf("%d",&t);
	for(i=0;i<t;i++){
	    c=0;
	    scanf("%d %d %d %d %d %d %d",&a1,&a2,&a3,&a4,&a5,&a6,&a7);
	    c=a1+a2+a3+a4+a5+a6+a7;
	    if(c>3)
	        printf("YES\n");
	    else
	        printf("NO\n");
	}
	return 0;
}


