class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        if (n == 0):
            return ''
        power = 1
        while (26**power < n):
            power += 1
        
        while (power > 0):
            if (n == 26**(power)):
                num = n
            else:
                num = int(n/26**(power-1))
            if (num > 0):
                dnum = num
                if (1):
                    if (dnum == 1):
                        result += 'A'
                    elif (dnum == 2):
                        result += 'B'
                    elif (dnum == 3):
                        result += 'C'
                    elif (dnum == 4):
                        result += 'D'
                    elif (dnum == 5):
                        result += 'E'
                    elif (dnum == 6):
                        result += 'F'
                    elif (dnum == 7):
                        result += 'G'
                    elif (dnum == 8):
                        result += 'H'
                    elif (dnum == 9):
                        result += 'I'
                    elif (dnum == 10):
                        result += 'J'
                    elif (dnum == 11):
                        result += 'K'
                    elif (dnum == 12):
                        result += 'L'
                    elif (dnum == 13):
                        result += 'M'
                    elif (dnum == 14):
                        result += 'N'
                    elif (dnum == 15):
                        result += 'O'
                    elif (dnum == 16):
                        result += 'P'
                    elif (dnum == 17):
                        result += 'Q'
                    elif (dnum == 18):
                        result += 'R'
                    elif (dnum == 19):
                        result += 'S'
                    elif (dnum == 20):
                        result += 'T'
                    elif (dnum == 21):
                        result += 'U'
                    elif (dnum == 22):
                        result += 'V'
                    elif (dnum == 23):
                        result += 'W'
                    elif (dnum == 24):
                        result += 'X'
                    elif (dnum == 25):
                        result += 'Y'
                    else:
                        result += 'Z'
                if (n > 26**(power-1)):
                    n = n%(26**(power-1))
                power -= 1
            else:
                if (result != ''):
                    result += 'A'
                power -= 1


        return result


