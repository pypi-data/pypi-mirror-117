import pickle
def save_v(v,filename):
  f=open(filename,'wb')
  pickle.dump(v,f)
  f.close()
  return filename
 
def load_v(filename):
  f=open(filename,'rb')
  r=pickle.load(f)
  f.close()
  return r