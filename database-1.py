class DataBase():
    def __init__(self):
        self.key = []
        self.value = []
        
    def return_key(self, value):
        for i in range(len(self.value)):
            if self.value[i] == value:
                return self.key[i]
            else:
                pass
    
    def return_value(self, key):
        for j in range(len(self.key)):
            if self.key[j] == key:
                return self.value[j]
            else:
                pass
    
    def return_key_and_value(self, num):
        try:
            return self.key[num-1], self.value[num-1]
        except:
            return "None"
    
    def add(self, key, value):
        self.key.append(key)
        self.value.append(value)
    
    def delete(self, num):
        del self.key[num]
        del self.value[num]
