# simple srt time converter
def time(j):
  if j < 60:                              # second
    sec = ",".join(('%.3f'%(j)).split('.'))
    return "00:00:" + sec		        
	
  elif j < 3600:                          # minute
    sec = j % 60 			       
    sec = ",".join(('%.3f'%(sec)).split('.'))
    mins = int(j/60)
    return "00:" + str(mins) + ":" + sec

  else:				  	  # hour
    sec = j % 60 			       
    sec = ",".join(('%.3f'%(sec)).split('.'))
    mins = int((j%3600)/60)
    hrs = int(j/3600)
    return str(hrs) + ":" + str(mins) + ":" + str(sec)


# use your time here
print time(75.32875610)
