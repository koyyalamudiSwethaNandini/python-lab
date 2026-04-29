class RevWords:

    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


rw = RevWords()
print(rw.reverse_words('welcome to python'))
