# class HashMap:
#     def __init__(self):
#         self.size = 10
#         self.hashlist = [None] * 10

#     def get_hashed_index(self, key):
#         return hash(key) % self.size


#     def __setitem__(self, key, value):
#         index = self.get_hashed_index(key)
#         if self.hashlist[index] is None:
#             self.hashlist[index] = [[key, value]]
#         else:
#             self.hashlist[index].append([key, value])

#     def Get(self, key):
#         index = self.get_hashed_index(key)
#         if self.hashlist[index]:
#             sublist = self.hashlist[index]
#             print(sublist)


class HashMap:
    def __init__(self):
        self.size = 10
        self.hashlist = [None] * self.size

    def getindex(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self.getindex(key)
        if self.hashlist[index] is None:
            self.hashlist[index] = [[key, value]]
        else:
            sublist = self.hashlist[index]
            for i in sublist:
                if i[0] == key:
                    i[1] = value
                    return
            self.hashlist[index].append([key, value])

    def __getitem__(self, key):
        index = self.getindex(key)

        if self.hashlist[index]:
            sublist = self.hashlist[index]
            for i in sublist:
                if i[0] == key:
                    return i[1]
        else:
            return "Nothing found!!"

    def __delitem__(self, key):
        index = self.getindex(key)
        if self.hashlist[index]:
            sublist = self.hashlist[index]
            for i in range(len(sublist)):
                if sublist[i][0] == key:
                    del sublist[i]
        else:
            return "Not found"


hm = HashMap()
hm["Name"] = "Amraz"
hm["Name"] = "Ambro"
print(hm.hashlist)
hm["Age"] = 19
hm["Phone number"] = 9947620637

print(hm["Name"])
del hm["Name"]
print(hm["Name"])

print(hm.hashlist)
