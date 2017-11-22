import numbers

def format_line(hash):
  outarr = []
  for k,v in hash.items():
    if v is None:
      outarr.append("%s=" % k)
      continue

    if isinstance(v, bool):
        v = "true" if v else "false"

    elif isinstance(v, numbers.Number ):
        pass

    else:
      if isinstance(v, (dict, object)):
        v = str(v)

      v = '"%s"' % v.replace('"', '\\' + '"')
    
    outarr.append("%s=%s" % (k, v))

  return " ".join(outarr)



