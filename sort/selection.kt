fun sort(n: MutableList<Int>) {
    var tmp: Int
    var minIndex: Int
    for(i in n.indices.filter({ it < n.size - 1 })) {
        minIndex = i
        n.indices.filter({ it >= i + 1 }).forEach({ j -> if(n[j] < n[minIndex]) minIndex = j })
        if(minIndex != i) {
            tmp = n[i]
            n[i] = n[minIndex]
            n[minIndex] = tmp
        }
    }
}