
def pow(a,b):
    return a**b

def distinct(a,b):
    terms = []
    for i in range(a,b+1):
        for j in range(a,b+1):
            product = pow(i,j)
            if product not in terms:
                terms.append(product)
    return len(terms)

print(distinct(2,100))
