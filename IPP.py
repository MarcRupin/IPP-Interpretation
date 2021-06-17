# IPP Finals Statistics
def main():
    num1 = float(input("Input the the number of respondents for Never."))
    num2 = float(input("Input the number of respondents for Almost Never"))
    num3 = float(input("Input the number of respondents for Sometimes"))
    num4 = float(input("Input the number of respondents for Fairly Often"))
    num5 = float(input("Input the number of respondents for Very Often"))
    weighted_num = ((num1 * 1) + (num2 * 2) + (num3 * 3) + (num4 * 4) + (num5 * 5))
    mean = weighted_num / (num1 + num2 + num3 + num4 + num5)
    var1 = (((((5 - mean) ** 2) * num5) + (((4 - mean) ** 2) * num4) + (((3 - mean) ** 2) * num3) + (((2 - mean) ** 2)
                                                                                                     * num2) + (((1 -
                                                                                                                  mean
                                                                                                                  ) ** 2
                                                                                                                 )
                                                                                                                * num1))
            / ((num1 + num2 + num3 + num4 + num5) - 1))
    stddev = var1 ** 0.5
    print(mean)
    print(var1)
    print(stddev)


if __name__ == '__main__':
    main()
