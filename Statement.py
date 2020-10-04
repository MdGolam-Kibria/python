totalMarks = 100
passMarks = 33
mcq = 30
cq = 3
total = float(mcq + cq)
if total < passMarks:
    print(f"you have {total} from {totalMarks}", end=" =  Fail")
elif total <= passMarks:
    print(f"you have {total} from {totalMarks}", end=" = Pass")
else:
    print(f"you have {total} from total", end=" = Pass")
