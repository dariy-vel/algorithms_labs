class Calendar:
    def __init__(self, input_list):
        self.output_list = []
        self.input_list = sorted(input_list)

    def add(self, input_tuple):
        if len(input_tuple) != 2:
            return
        if len(self.output_list) == 0:
            self.output_list.append(input_tuple)
        elif self.output_list[-1][0] <= input_tuple[1] < self.output_list[-1][1]:
            self.output_list[-1] = (input_tuple[0], self.output_list[-1][1])
        elif input_tuple[0] <= self.output_list[-1][1] < input_tuple[1]:
            self.output_list[-1] = (self.output_list[-1][0], input_tuple[1])
        else:
            self.output_list.append(input_tuple)

    def optimize(self):
        for item in self.input_list:
            self.add(item)
