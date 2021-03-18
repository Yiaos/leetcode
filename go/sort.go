package main

import (
	"fmt"
)

func HeapSort(lst []int) {
	m := (len(lst) - 2) / 2

	for i := m; i > -1; i-- {
		heap(lst, len(lst), i)
	}

	for i := len(lst) - 1; i > 0; i-- {
		lst[i], lst[0] = lst[0], lst[i]
		heap(lst, i, 0)
	}
}

func heap(lst []int, size, root int) {
	child := root*2 + 1
	if child >= size {
		return
	}

	if child+1 < size && lst[child] < lst[child+1] {
		child++
	}
	if lst[child] > lst[root] {
		lst[child], lst[root] = lst[root], lst[child]
	} else {
		return
	}
	heap(lst, size, child)

}

func main() {
	lst := []int{
		3, 23, 242, 67, 343, 3, 7, 8, 43, 5, 6, 73, 3, 455, 53,
	}
	HeapSort(lst)
	fmt.Println(lst)
}
