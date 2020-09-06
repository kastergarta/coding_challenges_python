class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = [int(i) for i in a[:-1].split('+')]
        b = [int(i) for i in b[:-1].split('+')]
        c = a[0] * b[0] - a[1] * b[1]
        d = a[0] * b[1] + a[1] * b[0]
        return str(c) + '+' + str(d) + 'i'