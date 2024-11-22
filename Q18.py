def print_odd (N :Node):
    if N == None:
        return
    if N.data % 2 !=0:
        print(N.data)
        print_odd(N.next)

  print_odd(l.head)