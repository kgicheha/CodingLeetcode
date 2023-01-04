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

//   adding edges or connection
  addEdge(vertex1, vertex2){
    if(this.adjacencyList[vertex1] && this.adjacencyList[vertex2]){
        this.adjacencyList[vertex1].push(vertex2)
        this.adjacencyList[vertex2].push(vertex1)
        return true
    }
    return false
  }
}

let myGraph = new Graph()
myGraph.addVertex('A')
myGraph.addVertex('B')

myGraph.addEdge("A", "B")
