PERMISSIONS_TABLE = {
"---": "0",
"--x": "1",
"-w-": "2",
"-wx": "3",
"r--": "4",
"r-x": "5",
"rw-": "6",
"rwx": "7"
}

def get_octal_from_file_permission(rwx: str) -> str:
    """Receive a Unix file permission and convert it to
       its octal representation.

       In Unix you have user, group and other permissions,
       each can have read (r), write (w), and execute (x)
       permissions expressed by r, w and x.

       Each has a number:
       r = 4
       w = 2
       x = 1

       So this leads to the following input/ outputs examples:
       rw-r--r-- => 644 (user = 4 + 2, group = 4, other = 4)
       rwxrwxrwx => 777 (user/group/other all have 4 + 2 + 1)
       r-xr-xr-- => 554 (user/group = 4 + 1, other = 4)
    """
    return ''.join([PERMISSIONS_TABLE[segment] for segment in (rwx[:3], rwx[3:6], rwx[6:])])