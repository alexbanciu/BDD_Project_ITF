"""
   O modalitate prin care putem sa dam un context general testelor noastre
   Functioneaza in pereche cu GIVEN
   Punem in Background orice element de context care este valabil pentru toate scenariile din feature file
   TAGS = daca vrem sa separam testele pe care le rulam si sa le executam individual sau grupate, atunci folosim conceptul de taguri
   Tag-urile incep cu semnul @ si sunt urmate de free text(este recomandat ca acesta sa fie sugestiv)
   Un scenariu poate fi identificat prin mai multe tag-uri
   In momentul rularii sciem astfel atunci cand folosim si tag-uri:
     e.g. behave -f html -o behave-report.html --tags=T1
     ==> va rula primul scenariu
   """