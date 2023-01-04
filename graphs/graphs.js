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

//   adding edges

}

let myGraph = new Graph()
myGraph.addVertex('A')