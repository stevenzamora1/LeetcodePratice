/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */

 function ListNode(val, next) {
      this.val = (val===undefined ? 0 : val)
      this.next = (next===undefined ? null : next)
 }


 class LinkedList {
    constructor() {
      this.head = null;
      this.size = 0;
    }
  
    // Insert first node
    insertFirst(data) {
      this.head = new Node(data, this.head);
      this.size++;
    }
}
var isPalindrome = function(head) {
    let current = this.head

    while(current){
        
        current = current.next
    }
};

const ll = new ListNode();
ll.insertFirst(10);
ll.insertFirst(400);
console.log(ll);
console.log("hello");