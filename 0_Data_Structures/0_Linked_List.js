class Node{

	constructor(givenData) {
		this.data = givenData;
}
	function printData(){
		console.log(this.data)
}

}

const first = new Node(9);
first.printData()
