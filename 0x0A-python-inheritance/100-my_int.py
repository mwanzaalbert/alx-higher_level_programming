code = '''
class MyInt(int):
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
'''

with open('100-my_int.py', 'w') as file:
    file.write(code)
