#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
int n,inorder[5111],postorder[5111];
void construct(int il,int ir,int pl,int pr){
    if(il>ir)return;
    int root=postorder[pr];
    cout<<root<<' ';
    int i=il;
    for(;inorder[i]!=root;i++);
    construct(il,i-1,pl,pl+i-il-1);
    construct(i+1,ir,pl+i-il,pr-1);
}
int main(){
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>inorder[i];
    for(int i=0;i<n;i++)
        cin>>postorder[i];
    construct(0,n-1,0,n-1);
    return 0;
}