# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]

def write_responses(result):
    print('\n'.join(result))

# def process_queries(queries):
#     result = []
#     # Keep list of all existing (i.e. not deleted yet) contacts.
#     contacts = []
#     for cur_query in queries:
#         if cur_query.type == 'add':
#             # if we already have contact with such number,
#             # we should rewrite contact's name
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     contact.name = cur_query.name
#                     break
#             else: # otherwise, just add it
#                 contacts.append(cur_query)
#         elif cur_query.type == 'del':
#             for j in range(len(contacts)):
#                 if contacts[j].number == cur_query.number:
#                     contacts.pop(j)
#                     break
#         else:
#             response = 'not found'
#             for contact in contacts:
#                 if contact.number == cur_query.number:
#                     response = contact.name
#                     break
#             result.append(response)
#     return result

def hash(number, m=10):
    a = 34
    b = 2
    p = 100003
    return ((((a*number) + b) % p) % m)

def hash_process_queries(queries):
    m = 10
    link = [[] for _ in range(m)]
    result = []

    for cur_query in queries:
        h = int(hash(int(cur_query.number)))

        if cur_query.type == 'add':
            for contact in link[h]:
                if contact[0] == cur_query.number:
                    contact[1] = cur_query.name
                    break
            else:
                link[h].append([cur_query.number, cur_query.name])

        elif cur_query.type == 'del':
            for j in range(len(link[h])):
                if link[h][j][0] == cur_query.number:
                    # print(link[h])
                    link[h].pop(j)
                    # print(link[h])
                    break

        else:
            response = 'not found'
            for contact in link[h]:
                if contact[0] == cur_query.number:
                    response = contact[1]
                    break
            result.append(response)
    return result


# if __name__ == '__main__':
#     write_responses(hash_process_queries(read_queries()))

class PhoneBook:
    def __init__(self):
        self.book = [None] * 10000000

    def add(self, number, name):
        self.book[number] = name

    def delete(self, number):
        if self.book[number] is not None:
            self.book[number] = None

    def find(self, number):
        if self.book[number] is None:
            return "not found"
        return self.book[number]


def process_queries(queries):
    for query in queries:
        q = query.split()
        cmd = q[0]
        number = int(q[1])
        if cmd == "add":
            phonebook.add(number, q[2])
        elif cmd == "find":
            print(phonebook.find(number))
        elif cmd == "del":
            phonebook.delete(number)


if __name__ == "__main__":
    phonebook = PhoneBook()

    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)


