class Solution:

    @staticmethod
    def reverse(number):
        one = int(number / 100)
        two = int(number % 100 / 10)
        three = int(number % 10)
        print(f"one {one} two {two} three {three}")
        return 100 * three + 10 * two + one


if __name__ == '__main__':
    result = Solution.reverse(123)
    print(result)
