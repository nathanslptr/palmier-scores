scores = {"Ines": 12900, "Bastien": 7430,"Karim": 31200, "Theo": 22750, "Marine": 18400, "Elise": 15680}
print("=== Classement des playstests ===")
for nom, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
    print(f"{nom:<10} {score:>7}")

moyenne = sum(scores.values()) / len(scores)
print(f"Moyenne : {moyenne:.0f}")
