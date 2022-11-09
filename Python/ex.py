"""
Dev: Prajwal Nautiyal
Last Update: 8 November 2022
Similar to its java counterpart, this program is also a recursive program.
"""

def main():
    i = GetInput()
    TowerOfHanoi(i[0], i[1], i[2], i[3])

def TowerOfHanoi(n , source, destination, auxiliary):
    if n == 1:
        print (f"Move disk 1 from {source} to destination {destination}")
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print (f"Move disk {n} from {source} to destination {destination}")
    TowerOfHanoi(n-1, auxiliary, destination, source)

def GetInput():
    print("Welcome to the Towers of Hanoi Game.")
    num = int(input("Enter the number of disces: "))
    src = input("Enter the initial position of discs: ")
    dest = input("Enter the destination for disces: ")
    aux = chr(ord(src) + 1)
    return num, src, dest, aux

main()