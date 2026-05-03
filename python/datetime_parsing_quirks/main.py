from dateutil import parser


s1 = "2026-04-13 15:30"
s2 = "April 13, 2026 3:30 PM"
s3 = "13/04/2026"

print(parser.parse(s1, dayfirst=True))
print(parser.parse(s2, dayfirst=True))
print(parser.parse(s3, dayfirst=True))