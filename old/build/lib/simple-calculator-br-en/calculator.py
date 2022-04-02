import numpy

class Calc:

    def sum(self, float_numbers):
        print(sum(float_numbers))

    def subtract(self, float_numbers):
        count = 0
        for i in float_numbers:
            if count == 0:
                sub = i

            if count > 0:
                sub -= i

            count+=1

        print(sub)
    def multiply(self, float_numbers):
        print(numpy.prod(float_numbers))

    def divide(self, float_numbers):
        count = 0
        for i in float_numbers:
            if count == 0:
                div = i

            if count > 0:
                div /= i

            count+=1

        print(div)