class Converter:
  def skaffArkiv(self):
    index = []
    for tall in range(8):
      index.append(2**tall)
    index.reverse()
    return index

  def convert(self, arr):
    referanse = self.skaffArkiv()
    rettetArr = []
    for letter in str(arr):
      rettetArr.append(int(letter))
    score = 0
    for teller in range(len(referanse)):
      score = score + referanse[teller]*rettetArr[teller]

    return score

  def binary(self, a):
    arkiv = self.skaffArkiv()
    
    counter = [];
    tallcounter = 0
    for teller in range(len(arkiv)):
      if tallcounter + arkiv[teller] <= a:
        tallcounter += arkiv[teller]
        counter.append("1")
      else:
        counter.append("0")
        continue
    
    return "".join(counter)

def start():
  instruksjon = input("Vil du konvertere til eller fra binary? (1 for til, 0 for fra)")

  session = Converter()
  if (int(instruksjon) == 1):
    print(session.binary(int(input("Hva vil du ha i binary?: "))))
  elif (int(instruksjon) == 0):
    print(session.convert(input("Hva vil du ha convertert fra binary?: ")))

start();
