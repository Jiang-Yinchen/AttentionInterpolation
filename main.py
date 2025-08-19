from fractions import Fraction

LANGUAGE = "Chinese"


def solve_linear_system(coefficients, constants):
    n = len(coefficients)
    A = [[Fraction(coeff) for coeff in row] for row in coefficients]
    B = [Fraction(const) for const in constants]

    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            B[j] -= factor * B[i]

    x = [Fraction(0)] * n
    for i in range(n-1, -1, -1):
        x[i] = B[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


def calculate_coefficient(n):
    c = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = (i + 1) ** j
    return c


if __name__ == '__main__':
    print({"Chinese": "请输入数列，以空行结束：", "English": "Please input a sequence, end with an empty line:"}[LANGUAGE])
    sequence = []
    length = 0
    while True:
        line = input()
        if line == "":
            break
        sequence.append(int(line))
        length += 1
    sol = solve_linear_system(calculate_coefficient(length), sequence)
    sol_str = ["" for i in range(length)]
    for i in range(length):
        if sol[i].numerator % sol[i].denominator == 0:
            sol_str[i] = str(sol[i].numerator // sol[i].denominator)
        elif sol[i].numerator > 0:
            sol_str[i] = "\\dfrac{" + str(sol[i].numerator) + "}{" + str(sol[i].denominator) + "}"
        else:
            sol_str[i] = "-\\dfrac{" + str(-sol[i].numerator) + "}{" + str(sol[i].denominator) + "}"
    res = ""
    for i in range(length):
        if sol_str[i] == "0":
            continue
        res = "+" + sol_str[i] + "x^{" + str(i) + "}" + res
    res = res.replace("+-", "-").replace("^{1}", "").replace("x^{0}", "")
    if len(res) == 0:
        res = "0"
    if res[0] == "+":
        res = res[1:]
    print(res)
    pass
