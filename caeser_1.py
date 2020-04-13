class Caeser:
    def __init__(self, shift):
        encoder = [0] * 26  # initiate with 0
        decoder = [0] * 26
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)  # This is a protected Attributes
        self._backward = ''.join(decoder)  # This is a protected Attributes

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        msg = list(original)
        for i in range(len(msg)):
            if msg[i].isupper():
                j = ord(msg[i]) - ord('A')  # msg[i]字符在Unicode中对应的整数代码点
                msg[i] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = Caeser(10000)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print(f'Secret: {coded}')
    answer = cipher.decrypt(coded)
    print(f'Answer: {answer}')
