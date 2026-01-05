s1 = "Ault"
s2 = "Kelly"

middle = len(s1) // 2  # Find the middle index of s1
s3 = s1[:middle] + s2 + s1[middle:]  # Insert s2 into the middle of s1
print(s3)  # Output: AuKellylt