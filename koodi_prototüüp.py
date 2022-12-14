import PySimpleGUI as sg
import os
#import matplotlib
from datetime import date

sg.theme('LightBrown2')

#kui kasutaja ei sisesta nime, siis error
paigutus = [[sg.Text('Andmed', text_color='black', font=("Helvetica", 12))],
          [sg.Text('Eesnimi: ')],
          [sg.InputText(key="eesnimi")],
          [sg.Text('Perekonnanimi: ')],
          [sg.InputText(key="perekonnanimi")],
          [sg.Text('_' * 80)],
          [sg.Submit('Graafik'), sg.Submit('Tulpdiagramm'), sg.Submit('Sektordiagramm'), sg.Cancel('Välju')]]
aken = sg.Window('Sinu andmed', paigutus, size=(400,200))
while True:
    syndmus, v22rtused = aken.read()
    #kui aken pannakse kinni, lõpetab programm töö
    if syndmus == sg.WIN_CLOSED or syndmus == 'Välju':
        break
    #kui vajutatakse nuppu 'Järgmine', pannakse põhiaken kinni ja avaneb uus aken
    if syndmus == 'Graafik':
        aken.close()
        
        
        #salvestame ees- ja perekonnanime muutujatesse
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
       
        
        #loome uue paigutuse uue akna jaoks
        #kasutame erinevaid elemente
        paigutus2 = [[sg.Text('Sisesta graafiku andmed', text_color='black', font=("Helvetica", 12))],
                  
                  [sg.Text('Sisesta graafiku nimetus: ')],
                  [sg.InputText(key="graafiknimi")],
                  [sg.Text('Sisesta väärtused (eralda semikoolonitega): ')],
                  [sg.InputText(key="graafikvaartus")],   
                  [sg.Text('_' * 80)],
                  [sg.Submit('Salvesta'), sg.Cancel('Välju')]]
   
        aken = sg.Window('Vajalikud anmded', paigutus2, size=(600,400))
        syndmus2, v22rtused2 = aken.read()
        
        graafiknimi = v22rtused2['graafiknimi']
        graafikvaartus = v22rtused2['graafikvaartus']
        
        
        #akna sulgemisel lõpetab programm töö
        if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Välju':
            break
        
        #kui vajutatakse nuppu 'Salvesta', pannakse põhiaken kinni ja avaneb uus aken
        if syndmus2 == 'Salvesta':
            aken.close()
            
            print(eesnimi, perekonnanimi) 
            print(graafiknimi, graafikvaartus) 
            
            
            
    if syndmus == 'Tulpdiagramm':
        aken.close()        
         
        #Esimese lehe salvestamine 
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
        
        #Uus aken
        paigutus3 = [[sg.Text('Sisesta tulpdiagrammi andmed', text_color='black', font=("Helvetica", 12))],
                  [sg.Text('Tulpade arv: ', size=(10,1)), sg.Slider(range=(1,8), orientation='h', size=(50,25), key='tulbad')],
                  [sg.Text('Sisesta nimetused (eralda komadega): ')],
                  [sg.InputText(key="nimetused")],
                  [sg.Text('Sisesta väärtused (eralda komadega): ')],
                  [sg.InputText(key="väärtused")],   
                  [sg.Text('_' * 80)],
                  [sg.Submit('Salvesta'), sg.Cancel('Välju')]]
        
        aken = sg.Window('Vajalikud anmded', paigutus3, size=(600,400))
        syndmus2, v22rtused2 = aken.read()
        
       
            
        #salvestame väärtused ja nimetused muutujatesse
        nimetused = v22rtused2['nimetused']
        väärtused = v22rtused2['väärtused']
        tulbad = v22rtused2['tulbad']
        
        
        #akna sulgemisel lõpetab programm töö
        if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Välju':
            break
        
        if syndmus2 == 'Salvesta':
            aken.close()
            print(eesnimi, perekonnanimi)
            print(nimetused, väärtused, tulbad)
            
            
    if syndmus == 'Sektordiagramm':
        aken.close()        
         
        #Esimese lehe salvestamine 
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
        
        #Uus aken
        paigutus4 = [[sg.Text('Sisesta sektordiagrammi andmed', text_color='black', font=("Helvetica", 12))],
                  [sg.Text('Sektorite arv: ', size=(10,1)), sg.Slider(range=(1,8), orientation='h', size=(50,25), key='sektorid')],
                  [sg.Text('Sisesta nimetused (eralda komadega): ')],
                  [sg.InputText(key="sektornimetused")],
                  [sg.Text('Sisesta väärtused (eralda komadega): ')],
                  [sg.InputText(key="sektorväärtused")],   
                  [sg.Text('_' * 80)],
                  [sg.Submit('Salvesta'), sg.Cancel('Välju')]]
        
        aken = sg.Window('Vajalikud anmded', paigutus4, size=(600,400))
        syndmus3, v22rtused3 = aken.read()
        
        sektornimetused = v22rtused3['sektornimetused']
        sektorväärtused = v22rtused3['sektorväärtused']
        sektoreid = v22rtused3['sektorid']
        
        
         #akna sulgemisel lõpetab programm töö
        if syndmus3 == sg.WIN_CLOSED or syndmus3 == 'Välju':
            break
        
        #kui vajutatakse nuppu 'Salvesta', pannakse põhiaken kinni ja avaneb uus aken
        if syndmus3 == 'Salvesta':
            aken.close()
            
            print(eesnimi, perekonnanimi)
            print(sektornimetused, sektorväärtused, sektoreid)
        
aken.close()
 
