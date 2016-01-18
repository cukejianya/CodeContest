def computeDifference(self):
    max_diff = 0
    arr = self.__elements
    for idx, main in enumerate(arr):
        for elm in arr[idx+1::]:
            diff = abs(main - elm)
            max_diff = max(diff, max_diff)

    self.maximumDifference = max_diff
