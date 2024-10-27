"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, <FULL NAME> and <FULL NAME>, this
programming assignment is my own work and I have not provided this code to
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1:
UT EID 2:
"""


class Node:
    """
    A modified version of the Node class for linked lists (using proper class
    coding practices). Instead of a data instance variable, this node class has both
    a coefficient and an exponent instance variable, which is used to represent each
    term in a polynomial.
    """

    def __init__(self, coeff, exp, link=None):
        """
        Node Constructor for polynomial linked lists.

        Args:
        - coeff: The coefficient of the term.
        - exp: The exponent of the term.
        - link: The next node in the linked list.
        """
        self.coeff = coeff
        self.exp = exp
        self.next = link

    @property
    def coeff(self):
        """
        Getter method for the coefficient attribute.
        """
        return self.__coeff

    @coeff.setter
    def coeff(self, value):
        """
        Setter method for the coefficient attribute.
        """
        if value is None or isinstance(value, int):
            self.__coeff = value
        else:
            raise ValueError("Coefficient must be an integer or None.")

    @property
    def exp(self):
        """
        Getter method for the exponent attribute.
        """
        return self.__exp

    @exp.setter
    def exp(self, value):
        """
        Setter method for the exponent attribute.
        """
        if value is None or isinstance(value, int):
            self.__exp = value
        else:
            raise ValueError("Exponent must be an integer or None.")

    @property
    def next(self):
        """
        Getter method for the next attribute.
        """
        return self.__next

    @next.setter
    def next(self, value):
        """
        Setter method for the next attribute.
        """
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise ValueError("Next must be a Node instance or None.")

    def __str__(self):
        """
        String representation of each term in a polynomial linked list.
        """
        return f"({self.coeff}, {self.exp})"


class LinkedList:
    def __init__(self):
        # You are also welcome to use a sentinel/dummy node!
        # It is definitely recommended, which will we learn more
        # about in class on Monday 10/21. If you choose to use
        # a dummy node, you can comment out the self.head = None
        # and comment in the below line. We use None to make sure
        # if there is an error where you accidentally include the
        # dummy node in your calculation, it will throw an error.
        # self.dummy = Node(None, None)
        self.head = None

    # Insert the term with the coefficient coeff and exponent exp into the polynomial.
    # If a term with that exponent already exists, add the coefficients together.
    # You must keep the terms in descending order by exponent.
    def insert_term(self, coeff, exp):
        
        if coeff == 0:
            return 

        new_term = Node(coeff, exp)
        
        # if empty
        if self.head is None:
            self.head = new_term
            self.head.next = None
            return
        
        # if its bigger than head exp
        if exp > self.head.exp:
            new_term.next = self.head
            self.head = new_term
            return

        current = self.head
        while current.next is not None and current.next.exp > exp:
            current = current.next

        if current.exp == exp:
            current.coeff += coeff
            if current.coeff == 0: 
                current.next = current.next.next # removes that node if the sum adds up to zero
        else:
            new_term = Node(coeff, exp, current.next)
            current.next = new_term
            

    # Add a polynomial p to the polynomial and return the resulting polynomial as a new linked list.
    def add(self, p):
        
        """possibilities
        if current poly is empty, add all of p
        if p is empty add all of current poly
        add in ascending order so
        if exp 1 > exp 2, add exp 1 term first,
        vice versa for if exp 2 > exp 1
        if neither, they are equal and add the coeff
        """
        
        sum = LinkedList()
        current_1 = self.head
        current_2 = p.head
        
        
        
        while current_1 is not None and current_2 is not None:
            if current_1 is None:
                sum.insert_term(current_2.coeff, current_2.exp)
                current_2 = current_2.next
                
            elif current_2 is None:
                sum.insert_term(current_1.coeff, current_1.exp)
                current_1 = current_1.next
                
            elif current_1.exp > current_2.exp:
                sum.insert_term(current_1.coeff, current_1.exp)
                current_1 = current_1.next
                
            elif current_2.exp > current_1.exp:
                sum.insert_term(current_2.coeff, current_2.exp)
                current_2 = current_2.next
                
            elif current_1.exp == current_2.exp:
                if (current_1.coeff + current_2.coeff) != 0:
                    sum.insert_term(current_1.coeff+current_2.coeff, current_1.exp)
                current_1 = current_1.next
                current_2 = current_2.next
        return sum

    # Multiply a polynomial p with the polynomial and return the product as a new linked list.
    def mult(self, p):
        
        prod = LinkedList()
        current_1 = self.head
        while current_1 is not None:
            # return p back to beginning after every loop
            current_2 = p.head

            # mult coeff add exp
            while current_2 is not None:
                mult_coeff = current_1.coeff * current_2.coeff
                mult_exp = current_1.exp + current_2.exp
                prod.insert_term(mult_coeff,mult_exp)
                current_2 = current_2.next
                
            current_1 = current_1.next
        return prod
        

    # Return a string representation of the polynomial.
    def __str__(self):
        current = self.head
        poly_str = ""
        while current.next is not None:
            poly_str += f"({current.coeff}, {current.exp}) + "
            current = current.next
        poly_str += f"({current.coeff}, {current.exp})"
        
        return poly_str



def main():
    # read data from stdin using input() and create polynomial p

    # read data from stdin using input() and create polynomial q

    # get sum of p and q as a new linked list and print sum

    # get product of p and q as a new linked list and print product
    
    polynomial_p = LinkedList()
    polynomial_q = LinkedList()
    
    # first line = length
    poly_length = int(input().strip())
    
    for i in range(poly_length):
        data = input().strip().split()
        coeff = int(data[0])
        exp = int(data[1])
        polynomial_p.insert_term(coeff, exp)
    
    # for the break line
    input()    
        
    poly_length = int(input().strip())
    for i in range(poly_length):
        data = input().strip().split()
        coeff = int(data[0])
        exp = int(data[1])
        polynomial_q.insert_term(coeff, exp)
    
    add_poly = polynomial_p.add(polynomial_q)
    print(add_poly)
    mult_poly = polynomial_p.mult(polynomial_q)
    print(mult_poly)
        


if __name__ == "__main__":
    main()