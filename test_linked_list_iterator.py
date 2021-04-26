from linked_list_iterator import LinkedList

def test_for_in_loop():
    
    hogwarts = LinkedList(('Harry', 'Hermione', 'Ron'))

    protagonists = []

    for student in hogwarts:
        protagonists.append(student)

    assert protagonists == ['Harry', 'Hermione', 'Ron']