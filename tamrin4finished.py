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
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(coeff, exp)

    def print(self):
        temp = self.head
        while temp:
            print(f"({temp.coeff})x^({temp.exp})", end='' if temp.next else '\n')
            temp = temp.next

    def print_result(self, polynomials, step):
        print("\nResult after step", step + 1, ":")
        polynomials[step].print()

def add_polynomials(head1, head2):
    dummy = Node(0, 0)
    curr = dummy
    while head1 and head2:
        if head1.exp > head2.exp:
            curr.next = head1
            head1 = head1.next
        elif head1.exp < head2.exp:
            curr.next = head2
            head2 = head2.next
        else:
            sum_coeff = head1.coeff + head2.coeff
            if sum_coeff:
                curr.next = Node(sum_coeff, head1.exp)
                curr = curr.next
            head1 = head1.next
            head2 = head2.next
        curr = curr.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return dummy.next

def multiply_polynomials(head1, head2):
    dummy = Node(0, 0)
    curr = dummy
    while head1:
        temp = head2
        while temp:
            product_coeff = head1.coeff * temp.coeff
            product_exp = head1.exp + temp.exp
            curr.next = Node(product_coeff, product_exp)
            curr = curr.next
            temp = temp.next
        head1 = head1.next
    return dummy.next

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
        exp = float(input("Enter exponent: "))
        polynomials[-1].insert(coeff, exp)
    elif choice == 2:
        index = int(input("Enter index of polynomial to delete: "))
        if 0 <= index < len(polynomials):
            polynomials.pop(index)
        else:
            print("\nInvalid index.")
    elif choice == 3:
        index = int(input("Enter index of polynomial to print: "))
        if 0 <= index < len(polynomials):
            print("\nPolynomial:")
            polynomials[index].print()
        else:
            print("\nInvalid index.")
    elif choice == 4:
        if len(polynomials) < 2:
            print("\nAdd at least 2 polynomials.")
        else:
            index1 = int(input("Enter index of first polynomial: "))
            index2 = int(input("Enter index of second polynomial: "))
            if 0 <= index1 < len(polynomials) and 0 <= index2 < len(polynomials):
                polynomials.append(LinkedList())
                polynomials[-1].head = add_polynomials(polynomials[index1].head, polynomials[index2].head)
    elif choice == 5:
        if len(polynomials) < 2:
            print("\nMultiply at least 2 polynomials.")
        else:
            index1 = int(input("Enter index of first polynomial: "))
            index2 = int(input("Enter index of second polynomial: "))
            if 0 <= index1 < len(polynomials) and 0 <= index2 < len(polynomials):
                polynomials.append(LinkedList())
                polynomials[-1].head = multiply_polynomials(polynomials[index1].head, polynomials[index2].head)
    elif choice == 6:
        break