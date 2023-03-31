
class Insurance():
    dataset = []
    def __init__(self,dataset):
        self.dataset = dataset
    def prediction(self,dataset):
        #Predict next value of dataset
        prediction = dataset[len(dataset)]
        return prediction
    def get_avg(self):
        avg = 0
        for i in self.dataset:
            avg =avg + i
        avg = avg / len(dataset)
        return avg
    def get_mode(self):
        max_freq = 0
        currently_freq = 0
        mode = -990000
        for i in range(1,len(self.dataset)):
            currently_freq = 0
            for j in range(i - 1,len(self.dataset) - 1):
                if(i == j):
                    currently_freq++
                    if(currently_freq > max_freq)
                        max_freq = currently_freq
                        mode = i
             

            


