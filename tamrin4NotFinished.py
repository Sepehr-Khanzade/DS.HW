class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, coeff, exp):
        if not self.head:
            self.head = Node(coeff, exp)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(coeff, exp)

    def delete(self, key):
        head_val = self.head.coeff
        if abs(head_val - key) <= 1e-5:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next:
            if abs(cur.next.coeff - key) <= 1e-5:
                cur.next = cur.next.next
                return
            cur = cur.next

    def print(self):
        cur = self.head
        while cur:
            print(cur.coeff, 'x^', cur.exp, end=' ')
            cur = cur.next
        print()

def add(llist1, llist2):
    dummy_node = Node(0, 0)
    current = dummy_node
    while llist1 and llist2:
        if llist1.head.exp > llist2.head.exp:
            current.next = llist1.head
            llist1.head = llist1.head.next
        elif llist1.head.exp < llist2.head.exp:
            current.next = llist2.head
            llist2.head = llist2.head.next
        else:
            sum_node = Node(llist1.head.coeff + llist2.head.coeff, llist1.head.exp)
            current.next = sum_node
            llist1.head = llist1.head.next
            llist2.head = llist2.head.next
        current = current.next
    if llist1:
        current.next = llist1.head
    if llist2:
        current.next = llist2.head
    return dummy_node.next

def multiply(llist1, llist2):
    dummy_node = Node(0, 0)
    current = dummy_node
    while llist1:
        llist3 = llist2
        while llist3:
            product_node = Node(llist1.head.coeff * llist3.head.coeff, llist1.head.exp + llist3.head.exp)
            current.next = product_node
            current = current.next
            llist3.head = llist3.head.next
        llist1.head = llist1.head.next
    return dummy_node.next

polynomials = []
while True:
    print("\n1. Insert Polynomial")
    print("2. Delete Polynomial")
    print("3. Print Polynomial")
    print("4. Add Polynomials")
    print("5. Multiply Polynomials")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        polynomials.append(LinkedList())
        coeff = float(input("Enter coefficient: "))
        exp = int(input("Enter exponent: "))
        polynomials[-1].insert(coeff, exp)
    elif choice == 2:
        polynomials.pop()
    elif choice == 3:
        if polynomials:
            print("\nPolynomial:")
            polynomials[0].print()
        else:
            print("\nNo polynomials to print.")
    elif choice == 4:
        if len(polynomials) < 2:
            print("\nAdd at least 2 polynomials.")
        else:
            print("\nPolynomial after addition:")
            add(polynomials[0], polynomials[1]).print()
    elif choice == 5:
        if len(polynomials) < 2:
            print("\nMultiply at least 2 polynomials.")


            