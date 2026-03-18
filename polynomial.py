from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Polynomial():
    coefficients: list[float] #index 0 is the coefficient of the degree zero term.
    degree: int = 2

    def __str__(self) -> str:
        return_string:str = 'y = '

        ##This should do a lot of coolified things to make this prettier, like
        # - Don't print coeffecients if they're 1
        # - Don't print term if coeffecient is 0
        # - Dynamically change sign (also including not printing leading +)
        for coeffecient, exponent in zip(reversed(self.coefficients), range(self.degree,-1,-1)):
            return_string += f"{coeffecient} * x^{exponent} + "
        return return_string
    
    def value(self: 'Polynomial', x: float) -> float:
        value = 0.0
        x_term = 1
        for coefficient in self.coefficients:
            value += coefficient*x_term
            x_term *= x
        return value

    def __add__(self, other:'Polynomial') -> 'Polynomial':
        ## Check which is higher degree and rename accordingly
        if self.degree > other.degree:
            higher = self
            lower = other
        else:
            higher = other
            lower = self

        #add coeffecients where both has terms
        new_coefficients = [lower.coefficients[i]+higher.coefficients[i] for i in range(0, lower.degree+1)]
        #Then append values from higher
        for i in range(lower.degree+2,higher.degree+1):
            new_coefficients.append(higher.coefficients[i])
        return Polynomial(coefficients=new_coefficients, degree=higher.degree)
    
    def __mul__(self, other:'Polynomial' | float | int):
        if isinstance(other,Polynomial):
            return self.poly_mult(other)
        elif isinstance(other,float | int):
            return self.scalar_mult(other)
        else:
            raise ValueError

    def scalar_mult(self, multiplier):
        ## Helper function for __mul__ implementation
        new_coefficients = [coeffecient * multiplier for coeffecient in self.coefficients]
        return Polynomial(coefficients=new_coefficients, degree=self.degree)
    
    def poly_mult(self, other:'Polynomial')-> 'Polynomial':
        ## Helper function for __mul__ implementation
        new_degree = self.degree + other.degree
        new_coefficients = [0]*(new_degree+1)
        for index_o, coefficent_o in enumerate(other.coefficients):
            for index_s, coefficent_s in enumerate(self.coefficients):
                new_coefficients[index_o+index_s] += coefficent_o*coefficent_s
        return Polynomial(coefficients=new_coefficients, degree= new_degree)

    def __sub__(self, other:'Polynomial') -> 'Polynomial':
    
        return self + (-other)
    
    def __neg__(self) -> Polynomial:
        return self.scalar_mult(-1)
    
class Poly2(Polynomial):
    def __init__(self,a:float | int=1,b:float | int=2,c:float | int=3):
        with_coefficients=[c,b,a]
        super().__init__(coefficients=with_coefficients)

    @property
    def a(self):
        return self.coefficients[2]
    
    @a.setter
    def a(self, to_value: float):
        self.coefficients[2] = to_value
    
    @property
    def b(self):
        return self.coefficients[1]
    
    @b.setter
    def b(self, to_value: float):
        self.coefficients[1] = to_value
    
    @property
    def c(self):
        return self.coefficients[0]
    
    @c.setter
    def c(self, to_value: float):
        self.coefficients[0] = to_value

    def __add__(self, other:'Poly2') -> 'Poly2':
        #Poly2 always has degree 2, so no extra checks needed
        new_coefficients = [self.coefficients[i]+other.coefficients[i] for i in range(0,2+1)]
        return Poly2(a=new_coefficients[2], b=new_coefficients[1], c=new_coefficients[0])

    def scale(self, factor:float | int) -> Poly2:
        return Poly2(a=self.coefficients[2]*factor, b=self.coefficients[1]*factor, c=self.coefficients[0]*factor)

    def __neg__(self) -> Poly2:
        return self.scale(-1)
    
    def __sub__(self, other:'Poly2') -> 'Poly2':
        return self + (-other)
    


def test_cases():
    print("A few print statements for testing purposes")
    my_poly = Poly2(1,5,-2)
    print(my_poly)

    my_poly.b=-2
    my_poly = my_poly.scalar_mult(10)

    my_second_poly = Poly2(2,1,4)
    base_poly = Poly2(1,1,1)
    print(my_poly+my_second_poly)
    print(my_poly-my_second_poly)
    print(base_poly*base_poly)
    print(base_poly*5)
    print(base_poly*2.3)
    print("Time for error")
    input("Press enter to continue, tests should cause a value error")
    print(base_poly*'Fel')

if __name__ == '__main__':
    test_cases()