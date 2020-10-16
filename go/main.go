package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"time"
)

type node struct {
	weight  int
	content string
	left    *node
	right   *node
}

// Given the node list, find the lightweight element (returning his idx in
// the slice
func minNode(nds []node) int {
	minIdx := -1
	lightest := int(^uint(0) >> 1) // max int
	for idx, n := range nds {
		if n.weight < lightest {
			lightest = n.weight
			minIdx = idx
		}
	}
	return minIdx
}

func toTree(n *node, dico *map[string]string, baseBit string) {
	if n.right == nil {
		(*dico)[n.content] = baseBit
	} else {
		toTree(n.right, dico, baseBit+"1")
	}
	if n.left == nil {
		(*dico)[n.content] = baseBit
	} else {
		toTree(n.left, dico, baseBit+"0")
	}
}

func main() {
	// Read file
	begin := time.Now()
	content, err := ioutil.ReadFile("./alice.txt")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Reading file: ", time.Since(begin))

	// Counting occurence
	begin = time.Now()
	occurence := make(map[string]int)
	for _, char := range content {
		chr := string(char)
		if _, ok := occurence[chr]; !ok {
			occurence[chr] = 1
		} else {
			occurence[chr]++
		}
	}
	fmt.Println("Counting occurence: ", time.Since(begin))

	// Making huffman tree
	begin = time.Now()
	nodes := make([]node, len(occurence))
	// Make all nodes
	idx := 0
	for chr, nb := range occurence {
		nodes[idx] = node{nb, chr, nil, nil}
		idx++
	}
	// Building the tree
	for len(nodes) > 1 {
		// Extract the first node
		minNodeIdx := minNode(nodes)
		n0 := nodes[minNodeIdx]
		nodes = append(nodes[:minNodeIdx], nodes[minNodeIdx+1:]...)
		// Extract second node
		minNodeIdx = minNode(nodes)
		n1 := nodes[minNodeIdx]
		nodes = append(nodes[:minNodeIdx], nodes[minNodeIdx+1:]...)

		// Make the new node
		nn := node{n0.weight + n1.weight, "", &n0, &n1}
		nodes = append(nodes, nn)
	}
	fmt.Println("Making huffman tree: ", time.Since(begin))

	// Re-encoding chars
	begin = time.Now()
	encoded := make(map[string]string)
	toTree(&nodes[0], &encoded, "")
	fmt.Println("Re-encoding chars: ", time.Since(begin))

	// Encode the text
	begin = time.Now()
	encodedContent := ""
	for _, char := range content {
		encodedContent += encoded[string(char)]
	}
	fmt.Println("Encoding the text: ", time.Since(begin))

	// Write the encoded content in file
	begin = time.Now()
	err = ioutil.WriteFile("output.txt", []byte(encodedContent), 0644)
	fmt.Println("Writing in file: ", time.Since(begin))
}
