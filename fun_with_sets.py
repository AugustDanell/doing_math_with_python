from sympy import FiniteSet, pprint

'''
    Modified examples from chapter 5, pertaining to sets.
    
    1-4:   Defining sets, cardinality and checking members in the set.
    5-7:   Alternative ways of declaring sets, declaring some subsets to use later.
    8-10:  Examples of how to use subsets.
    10-12: Examples of how to use supersets.
    13-14: Examples of how to use powersets, what they are and their cardinality.
    15-18: Examples of how to use intersection and union.
    19:    Example of how to use cartesian product. 
    
    Using format string where {<index>} are simply placeholders.
'''

print('Defining a set s and using some elementary operations:')
s = FiniteSet(3, 5, 7, 9)
print("1. Set S: {0}".format(s.__str__()))
print('2. Cardinality: %d' %(len(s)))
print('3. Is 6 in the set?: %r' %(4 in s))
s = FiniteSet(*[3,5,7,9,5])
print('4. Insertion another "5" into set s, but since it is a set it remains the same, s = {0}'.format(s.__str__()))

print()
print('Defining other sets, sets s2 and t:')
s2 = FiniteSet(*[3,5,7,9])
print('5. Defining set s2 = {0}'.format(s2))
print('6. Testing if s == s2: {0}'.format(s == s2))
t = FiniteSet(*[3,5,7])
print('7. Defining t as a subset of s, t = {0}'.format(t))

print()
print('Playing with subsets:')
print('8. Is s a subset of t? s.is_subset(t): {0}'.format(s.is_subset(t)))
print('9. Is t a subset of s? t.is_subset(s): {0}'.format(t.is_subset(s)))
print('10. Is s a subset of itself? s.is_subset(s): {0}'.format(s.is_subset(s)))

print()
print('Playing with supersets:')
print('11. Is s a superset of t? s.is_superset(t): {0}'.format(s.is_superset(t)))
print('12. Is t a superset of s? t.is_superset(s): {0}'.format(t.is_superset(s)))

print()
print('Playing with powersets (Sets of all subsets, including the empty set):')
T = t.powerset()
print('13. Defining T as a powerset to t, T = t.powerset(): {0}'.format(T))
print('14. What is the cardinality of T? It is 2^(cardinality_t), that is 2^3 = 8. len(T): {0}'.format(len(T)))

print()
print('Playing with Union and Intersections:')
s3 = FiniteSet(*[1, 2, 3])
print('15. Set S3 = {0}'.format(s3))
s4 = FiniteSet(*[3, 4, 5])
print('16. Set S4 = {0}'.format(s4))
print('17. Intersection of S3 and S4 consists of the element 3, s3.intersect(S4): {0}'.format(s3.intersect(s4)))
print('18. Union of S3 and S4 yields elements 1-5: {0}'.format(s3.union(s4)))

print()
print('19. Playing with Cartesian products (All possible pairs of s3 and s4):')
cartesian_product = s3*s4
for e in cartesian_product:
    print(e)
