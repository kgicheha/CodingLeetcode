/*
Creating a BINARY SEARCH TREE using JavaScript
*/

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(value) {
    //create new Node using the Node Class
    const newNode = new Node(value);
    // if the roor is null, meaning the tree is empty
    // set the root equal to the new Node
    if (this.root === null) {
      this.root = newNode;
      return this;
    }

    // create a temporary variable that store the current value of the root
    let temp = this.root;

    // keep looping until it becomes false
    while (true) {
      // if a value already exists in the tree, return undefined
      if (newNode.value === temp.value) {
        return undefined;
      }
      // if the value of the new node is less than the value of the root, go left
      if (newNode.value < temp.value) {
        // if temp.left is null, set temp.left equal to new Node
        // else set temp equal to temp.left and repeat the process
        if (temp.left === null) {
          temp.left = newNode;
          return this;
        }
        temp = temp.left;
      } else {
        if (temp.right === null) {
          temp.right = newNode;
          return this;
        }
        temp = temp.right;
      }
    }
  }

  contains(value) {
    if (this.root === null) {
      return false;
    }

    let temp = this.root;

    while (temp) {
      if (value < temp.value) {
        temp = temp.left;
      } else if (value > temp.value) {
        temp = temp.right;
      } else {
        return true;
      }
    }
    return false;
  }

// returns the minimum value
  minValue(currentNode){
    while (currentNode.left != null){
        currentNode = currentNode.left
    }
    return currentNode
  }
}

let myTree = new BST();
