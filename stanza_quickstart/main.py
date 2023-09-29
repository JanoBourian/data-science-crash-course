import stanza
import time 

initial = time.perf_counter()
stanza.download("es")
nlp = stanza.Pipeline("es")
doc = nlp("Mexico es un excelente pais")
print("***** DOC *****")
print(doc)
print("***** ENTITIES *****")
print(doc.entities)
print(f"TOTAL TIME: {time.perf_counter() - initial}")