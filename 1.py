def CreateLuhnAlgorithm(card):
    nNumber = len(card)
    nSum = 0
    ScondNum = False

    for i in range(nNumber - 1, -1, -1):
        d = ord(card[i]) - ord('0')

        if (ScondNum == True):
            d = d * 2


        nSum += d // 10
        nSum += d % 10

        ScondNum = not ScondNum

    if (nSum % 10 == 0):
        return True
    else:
        return False


if __name__ == "__main__":

    card = "12345678910"

    if (CreateLuhnAlgorithm(card)):
        print("This is a valid card number")
    else:
        print("This isn't valid card number")

#