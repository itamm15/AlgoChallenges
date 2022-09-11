#include <iostream>
#include <queue>

struct Node{
    int data;
    Node *left;
    Node *right;
};

Node *createNode(int data){
    Node *newNode = new Node();
    newNode->data = data;
    newNode->left = newNode->right = nullptr;
    return newNode;
}

Node *search(Node *root, int key){
    if(root == nullptr){
        return nullptr;
    }

    std::queue< Node* > q;
    Node *out = nullptr;
    q.push(root);

    while(!q.empty()){
        Node *tmp = q.front();
        q.pop();
        if(tmp->data == key){
            out = tmp;
            std::cout << "Key has been found!" << std::endl;
        } 
        if(tmp->left != nullptr) q.push(tmp->left);
        if(tmp->right !=nullptr) q.push(tmp->right);
    }
    return out;

}

int main(){
    
    Node *root = createNode(1);
    root->left = createNode(2);
    root->left->left = createNode(4);
    root->right = createNode(3);
    root->right->right = createNode(5);

    Node *node = search(root, 7);
    std::cout << &node << std::endl;
}

// Searching the node with given value
// The search function ought to return the pointer TO THE GIVEN POINTER