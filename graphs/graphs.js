class Graph {
  // creating new graph
  constructor() {
    this.adjacencyList = {};
  }

  // adding vertex or node
  // if there isn't a vertex in the list with this value
    // add it to the list
    // set its value equal to an empty array
  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) {
      this.adjacencyList[vertex] = [];
      return true
    }
    return false
  }

//   adding edge or connection
  addEdge(vertex1, vertex2){
    if(this.adjacencyList[vertex1] && this.adjacencyList[vertex2]){
        this.adjacencyList[vertex1].push(vertex2)
        this.adjacencyList[vertex2].push(vertex1)
        return true
    }
    return false
  }


//   removing edge or connection
//   use the filter to return everything that not equal to the given vertext
  removeEdge(vertex1, vertex2){
    if(this.adjacencyList[vertex1] && this.adjacencyList[vertex2]){
        this.adjacencyList[vertex1] = this.adjacencyList[vertex1]
            .filter(v => v !== vertex2)

        this.adjacencyList[vertex2] = this.adjacencyList[vertex2]
            .filter(v => v !== vertex1)

        return true
      }
      return false
    }

    // removing vertex or nodes
        // if vertex doesnt exist in the object, return undefined
        // remove edges first, then remove the vertex
        // while the length of array is more than 0
            // save the last element in the array to a temp variable
            // use the REMOVEEDGE method to remove the edges between the given vertex and the temp vertex

    removeVertex(vertex){
        if(!this.adjacencyList[vertex]) return undefined

        while(this.adjacencyList[vertex].length){
            let temp = this.adjacencyList[vertex].pop()
            this.removeEdge(vertex, temp)
        }
        delete this.adjacencyList[vertex]
        return this
    }

}

let myGraph = new Graph()
myGraph.addVertex('A')
myGraph.addVertex('B')

myGraph.addEdge("A", "B")
