guests = ['mom', 'dad', 'laura', 'chuck', 'dj']
print("Please join me for dinner tonight, " + guests[0].title() + ".")
print("Please join me for dinner tonight, " + guests[1].title() + ".")
print("Please join me for dinner tonight, " + guests[2].title() + ".")
print("Please join me for dinner tonight, " + guests[3].title() + ".")
print("Please join me for dinner tonight, " + guests[4].upper() + ".")
print("\nUnfortunately, " + guests[3].title() + " cannot attend.")
guests[3] = 'cindy'
print("\nPlease join me for dinner tonight, " + guests[0].title() + ".")
print("Please join me for dinner tonight, " + guests[1].title() + ".")
print("Please join me for dinner tonight, " + guests[2].title() + ".")
print("Please join me for dinner tonight, " + guests[3].title() + ".")
print("Please join me for dinner tonight, " + guests[4].upper() + ".")
print("\nI found a larger dinner table!")
guests.insert(0, 'layla')
guests.insert(3, 'luke')
guests.append('mark')
print("\nPlease join me for dinner tonight, " + guests[0].title() + ".")
print("Please join me for dinner tonight, " + guests[1].title() + ".")
print("Please join me for dinner tonight, " + guests[2].title() + ".")
print("Please join me for dinner tonight, " + guests[3].title() + ".")
print("Please join me for dinner tonight, " + guests[4].title() + ".")
print("Please join me for dinner tonight, " + guests[5].title() + ".")
print("Please join me for dinner tonight, " + guests[6].upper() + ".")
print("Please join me for dinner tonight, " + guests[7].title() + ".")