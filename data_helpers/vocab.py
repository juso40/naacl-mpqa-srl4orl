import re

PAD = "PADDING"
UNK = "UNKNOWN"
RE_NUM = re.compile("[0-9]")


class Vocab(object):
    #################################
    # Mapping between words and IDs #
    #################################

    def __init__(self):
        self.i2w = []
        self.w2i = {}

    def add_word(self, word):
        if word not in self.w2i:
            new_id = self.size()
            self.i2w.append(word)
            self.w2i[word] = new_id

    def get_id(self, word):
        return self.w2i.get(word)

    def get_word(self, w_id):
        return self.i2w[w_id]

    def has_key(self, word):
        return self.w2i.has_key(word)

    def size(self):
        return len(self.i2w)

    def save(self, path):
        with open(path, 'w') as f:
            for i, w in enumerate(self.i2w):
                print(str(i) + '\t' + w.encode('utf-8'), file=f)

    @classmethod
    def load(cls, path):
        vocab = Vocab()
        with open(path) as f:
            for line in f:
                w = line.strip().split('\t')[1].decode('utf-8')
                vocab.add_word(w)
        return vocab

