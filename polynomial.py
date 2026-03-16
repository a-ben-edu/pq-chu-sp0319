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
    
    def scalar_mult(self, multiplier):
        new_coefficients = [coeffecient * multiplier for coeffecient in self.coefficients]
        return Polynomial(coefficients=new_coefficients, degree=self.degree)
    
    def __sub__(self, other:'Polynomial') -> 'Polynomial':
        other_inverted = other.scalar_mult(-1)
        return self + other_inverted
    
class Poly2(Polynomial):
    def __init__(self,a=1,b=2,c=3):
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

    
    

my_poly = Poly2(1,5,-2)
print(my_poly)

my_poly.b=-2
my_poly = my_poly.scalar_mult(10)

my_second_poly = Poly2(2,1,4)
print(my_poly+my_second_poly)
print(my_poly-my_second_poly)