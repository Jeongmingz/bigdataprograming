def print_kwargs(**kwargs):
    print("Keyword arguments", kwargs)


print_kwargs(
    fruits='apple',
    coffee='latte'
)


def print_data(data, *, start=0, end=100):
    # * => 가변의 갯수를 받는다.
    for value in (data[start:end]):
        print(value, end=' ')


data = ['a', 'b', 'c', 'd', 'e', 'f']

print_data(data)
