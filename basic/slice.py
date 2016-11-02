str = 'X-DSPAM-Confidence: 0.8475'
val=float(str[str.find(':')+2:])
print('The float value is %g' % val)
