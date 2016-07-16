from flask import Flask, request

app = Flask(__name__)

def main(my_input='test'):
    # do whatever you want here
    return 'returned from main: {0}'.format(my_input)

@app.route("/", methods=['GET', 'POST'])
def run_script():
    if request.form:
        output = main(request.form['my_input'])
    else:
        output = ''

    return """
        Enter Your Input:</br>
        <form method="POST">
            <input name="my_input">
            <input type="submit" value="Submit">
        </form></br>
        Output:</br>
        """ + output

if __name__ == "__main__":
    class Multiples(object):
        def __init__(self, divisors=[], limit=100):
            self.divisors = divisors
            self.limit = limit

        def add_divisor(self, div):
            self.divisors.append(div)

        @property
        def divisors_as_string(self):
            return ', '.join((str(d) for d in self.divisors[:-1])) + ' and {0}'.format(self.divisors[-1])

        @property
        def sum_multiples(self):
            return sum(i for i in range(self.limit) if any(i % d == 0 for d in self.divisors))

        def __str__(self):
            return 'Sum of all the found multiples of {self.divisors_as_string} (below {self.limit}) is {self.sum_multiples}'.format(self=self)

    divisors = [3, 5, 7, 11, 19]
    limit = 100000
    mults = Multiples(divisors, limit)
    print(mults)
    mults.add_divisor(13)
    print(mults)
