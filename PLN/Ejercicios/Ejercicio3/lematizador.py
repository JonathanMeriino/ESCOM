#~ import freeling
from Preprocesamiento.utilidades import freeling
import sys, re

## ----------------------------------------------
## -------------    MAIN PROGRAM  ---------------
## ----------------------------------------------

## Modify this line to be your FreeLing installation directory
FREELINGDIR = "/usr/local";

DATA = FREELINGDIR+"/share/freeling/";
LANG="es";

freeling.util_init_locale("default");

# create language analyzer
la=freeling.lang_ident(DATA+"common/lang_ident/ident.dat");

# create options set for maco analyzer. Default values are Ok, except for data files.
op= freeling.maco_options("es");
op.set_data_files( "", 
                   DATA + "common/punct.dat",
                   DATA + LANG + "/dicc.src",
                   DATA + LANG + "/afixos.dat",
                   "",
                   DATA + LANG + "/locucions.dat", 
                   DATA + LANG + "/np.dat",
                   DATA + LANG + "/quantities.dat",
                   DATA + LANG + "/probabilitats.dat");

# create analyzers
tk=freeling.tokenizer(DATA+LANG+"/tokenizer.dat");
sp=freeling.splitter(DATA+LANG+"/splitter.dat");
sid=sp.open_session();
mf=freeling.maco(op);

# activate mmorpho odules to be used in next call 
mf.set_active_options(False, # Usermap 
                      False,  # NumbersDetection
                      True,  # PunctuationDetection
                      False,  # DatesDetection
                      True,  # DictionarySearch
                      True,  # AffixAnalysis 
                      False, # CompoundFile
                      True,   
                      True,  # MultiwordsDetection
                      True,  # NE Recognition 
                      True,  # QuantitiesDetection 
                      True   # ProbabilityAssignment
                      ); 

#~ umap: 'bool', num: 'bool', pun: 'bool', dat: 'bool', dic: 'bool', aff: 'bool', comp: 'bool', rtk: 'bool', mw: 'bool', ner: 'bool', qt: 'bool', prb: 'bool'
                      
0,# UserMap
						#~ 1,# AffixAnalysis
						#~ 1,# MultiwordsDetection
						#~ 0,# NumbersDetection
						#~ 1,# PunctuationDetection
						#~ 0,# DatesDetection
						#~ 1,# QuantitiesDetection
						#~ 1,# DictionarySearch
						#~ 1,# ProbabilityAssignment
						#~ 1);# NE Recognition

# create tagger, sense anotator, and parsers
tg=freeling.hmm_tagger(DATA+LANG+"/tagger.dat",True,2);
sen=freeling.senses(DATA+LANG+"/senses.dat");
parser= freeling.chart_parser(DATA+LANG+"/chunker/grammar-chunk.dat");
dep=freeling.dep_txala(DATA+LANG+"/dep_txala/dependences.dat", parser.get_start_symbol());


def lematizar(linea):		
	
	punto_agregado = False
	if not re.search(r"[\.$]",linea):
		linea = linea + "."
		punto_agregado = True
	
	palabras = tk.tokenize(linea)
	ls = sp.split(sid,palabras,False)
	ls = mf.analyze(ls)
	resultado = ''
	for s in ls :
		ws = s.get_words()
		for w in ws :
			resultado += w.get_lemma() + ' '
			#~ resultado += w.get_form() + ' '
			#w.get_form()+" "+w.get_lemma()+" "+w.get_tag()
	resultado = re.sub('\s+', ' ', resultado)
	if punto_agregado:
		resultado = re.sub('\.', '', resultado)
	
	return (resultado)
	
