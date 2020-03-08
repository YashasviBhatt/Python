principal=float(input('Enter Principal Amount : '))
rate=float(input('Enter Rate of Interest : '))
time=float(input('Enter Time Period : '))

si=lambda si : (principal*rate*time)/100

print('The Simple Interest of\nPrinciple Amount : {}'
      '\nRate of Interest : {}'
      '\nTime Period : {}'
      '\nis {}'
      .format(principal,rate,time,si(0)))