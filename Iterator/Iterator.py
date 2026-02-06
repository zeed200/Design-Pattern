class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        else:
            raise StopIteration()

class Sentence:
    def __init__(self, text):
        self.words = text.split()

    def __iter__(self):
        return SentenceIterator(self.words)


my_sentence = Sentence("Abdulrahman Mohammed")
for word in my_sentence:
    print(word)


#in django 

# مثال: إرسال بريد إلكتروني لمليون مستخدم
large_queryset = User.objects.all().iterator(chunk_size=1000)

for user in large_queryset:
    # المعالجة تتم مستخدم بمستخدم
    # Django يجلب 1000 مستخدم فقط في كل مرة ليحافظ على الذاكرة
    send_welcome_email(user.email)    