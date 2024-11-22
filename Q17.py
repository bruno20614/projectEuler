from ctypes.wintypes import SIZEL

from Q16 import LinkedList


def dividirLista(L):

    SI = FS = L.head

    while SI.next: != None
        SI = SI.next
        FS = FS.next
        if FS == None
            break
        FS = FS.next

    L2 = LinkedList()
    LS.head = SI
    SI.next = None

    return L,L2