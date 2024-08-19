# FreeCodeCamp Learn Interfaces by Building an Equation Solver
# Completed 8/19/2024
# Comments added for clarity post-lesson.

from abc import ABC, abstractmethod
import re

# Abstract base class for different types of equations
class Equation(ABC):
    degree: int  # Degree of the equation
    type: str  # Type of the equation (e.g., 'Linear Equation')

    # Constructor to validate and store coefficients
    def __init__(self, *args):
        # Ensure the number of arguments matches the degree of the equation plus one
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        # Ensure all coefficients are either integers or floats
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        # Ensure the highest degree coefficient is not zero
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        # Store coefficients in a dictionary, mapping the degree to the coefficient value
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    # Ensure subclasses have required attributes ('degree' and 'type')
    def __init_subclass__(cls):
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    # String representation of the equation
    def __str__(self):
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:  # Skip terms with a coefficient of 0
                continue
            if n == 0:
                terms.append(f'{coefficient:+}')  # Constant term
            elif n == 1:
                terms.append(f'{coefficient:+}x')  # First degree term
            else:
                terms.append(f"{coefficient:+}x**{n}")  # Higher degree terms
        equation_string = ' '.join(terms) + ' = 0'
        # Remove '1' from coefficients (e.g., '1x' becomes 'x')
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))        

    @abstractmethod
    def solve(self):
        pass  # Abstract method to be implemented by subclasses for solving the equation
        
    @abstractmethod
    def analyze(self):
        pass  # Abstract method to be implemented by subclasses for analyzing the equation


# Class for linear equations (degree = 1)
class LinearEquation(Equation):
    degree = 1
    type = 'Linear Equation'
    
    # Solve the linear equation ax + b = 0, returning the root x
    def solve(self):
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

    # Analyze the equation to return the slope and y-intercept
    def analyze(self):
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}


# Class for quadratic equations (degree = 2)
class QuadraticEquation(Equation):
    degree = 2
    type = 'Quadratic Equation'

    # Constructor that also calculates the discriminant (delta)
    def __init__(self, *args):
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c

    # Solve the quadratic equation ax^2 + bx + c = 0
    def solve(self):
        if self.delta < 0:  # No real roots
            return []
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)  # First root
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)  # Second root
        if self.delta == 0:  # Only one root when delta is 0
            return [x1]

        return [x1, x2]  # Return both roots

    # Analyze the equation to return the vertex and concavity
    def analyze(self):
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)  # x-coordinate of the vertex
        y = a * x**2 + b * x + c  # y-coordinate of the vertex
        if a > 0:
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}


# Function to solve and analyze an equation
def solver(equation):
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    # Format and return the output string with equation details
    output_string = f'\n{equation.type:-^24}'  # Equation type centered with hyphens
    output_string += f'\n\n{equation!s:^24}\n\n'  # Equation itself centered
    output_string += f'{"Solutions":-^24}\n\n'
    
    # Solve the equation and format the solutions
    results = equation.solve()
    match results:
        case []:  # No real roots
            result_list = ['No real roots']
        case [x]:  # One root
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]:  # Two roots
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']
    for result in result_list:
        output_string += f'{result:^24}\n'
    
    # Add details of the equation analysis
    output_string += f'\n{"Details":-^24}\n\n'
    details = equation.analyze()
    match details:
        case {'slope': slope, 'intercept': intercept}:  # Linear equation details
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:  # Quadratic equation details
            coord = f'({x:.3f}, {y:.3f})'
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {coord:>18}']
    for detail in details_list:
        output_string += f'{detail}\n'
    
    return output_string

# Input for testing the solver with linear and quadratic equations
lin_eq = LinearEquation(2, 3)
quadr_eq = QuadraticEquation(1, 2, 1)

# Solve and print the results for the quadratic and linear equations
print(solver(quadr_eq))
print(solver(lin_eq))