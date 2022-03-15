class ContaParole:
  def __init__(self):
    self.testo = ""
    self.tlist = []
    self.testo_pulito = ""
    self.tdict = {}

  def leggi_file(self,file_path):
    pass
  
  def scrivi_file(self, file_path):
    pass

  def conta_occorrenze(self, testo):
    self.testo = testo

    self.togli_punteggiatura()
    self.togli_spazi()
    self.conteggio()

  def togli_punteggiatura(self):
    self.testo_pulito = self.testo[:]
    
    for s in [",", ".", "!", "?", ":", ";"]:
      self.testo_pulito = self.testo_pulito.replace(s, "")

  def togli_spazi(self):
    self.tlist =  self.testo_pulito.split(" ")

  def conteggio(self):
    self.tdict = {}
    for k in self.tlist:
      if k in self.tdict:
        self.tdict[k] = self.tdict[k] + 1
      else:
        self.tdict[k] = 1

  def stampa_dict(self):
    for k, v in self.tdict.items():
      print(k, ": ", v)

# contare le occorrenze --> contare per ogni parola, quante volte compare all'interno del testo
testo = ""

cp = ContaParole()
cp.conta_occorrenze(testo)
cp.stampa_dict()
