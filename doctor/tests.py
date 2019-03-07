

# Create your tests here.
import time,hashlib


def create_id():
    m = hashlib.md5(str(time.time()).encode('utf-8'))
    return m.hexdigest()


if __name__ == '__main__':
    print(type(create_id()))
    print(time.time())
    print(create_id())
    print(create_id())
