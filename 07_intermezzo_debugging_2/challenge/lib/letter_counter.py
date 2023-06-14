class LetterCounter:
    def __init__(self, text):
        self.text = text.lower()

    def calculate_most_common(self):
        counter = {}
        most_common = []
        most_common_count = 0
        for char in self.text:
            if not char.isalpha():
                continue
            counter[char] = counter.get(char, 0) + 1
            if counter[char] == most_common_count:
                most_common.append(char)
            if counter[char] > most_common_count:
                most_common = [char]
                most_common_count = counter[char]
        return [most_common_count, most_common]


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())