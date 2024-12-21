MIN_AGE = 25
MIN_QUALIFICATION = ["bachelors", "masters", "diploma"]
MIN_EXPERIENCE = 3


def is_shortlisted(age, qualification, experience):
    return age >= MIN_AGE and qualification in MIN_QUALIFICATION and experience >= MIN_EXPERIENCE



num_candidates = int(input("Enter number of candidates: "))

shortlisted = []
rejected = []

for i in range(num_candidates):
    print(f"\nCandidate {i+1}:")
    name = input("Enter candidate name: ")
    age = int(input("Enter candidate age: "))
    qualification = input("Enter candidate qualification: ")
    experience = int(input("Enter candidate years of experience: "))
    
   
    if is_shortlisted(age, qualification, experience):
        shortlisted.append(name)
    else:
        rejected.append(name)


print("\nSummary of Candidates:")
print("Shortlisted Candidates:", shortlisted)
print("Rejected Candidates:", rejected)
