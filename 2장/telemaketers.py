pnumLast4First = input()
if len(pnumLast4First) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4First.isdigit():
    exit("문자열이 숫자가 아님")

pnumLast4Second = input()
if len(pnumLast4Second) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4Second.isdigit():
    exit("문자열이 숫자가 아님")

pnumLast4Third = input()
if len(pnumLast4Third) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4Third.isdigit():
    exit("문자열이 숫자가 아님")

pnumLast4Fourth = input()
if len(pnumLast4Fourth) != 1:
    exit("문자열의 길이는 1이어야 함")
if not pnumLast4Fourth.isdigit():
    exit("문자열이 숫자가 아님")

if not pnumLast4First in "89":
    exit("answer")

if not pnumLast4Fourth in "89":
    exit("answer")

if not pnumLast4Second == pnumLast4Third:
    exit("answer")

print("ignore")