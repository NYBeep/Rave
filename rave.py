import PySimpleGUI as sg
# import os
import matplotlib
import matplotlib.pyplot as plt
# from datetime import date
import numpy as np


sg.theme('LightBrown2')

#kui kasutaja ei sisesta nime, siis error
paigutus = [[sg.Text('Andmed', text_color='black', font=("Helvetica", 12))],
          [sg.Text('Eesnimi: ')],
          [sg.InputText(key="eesnimi")],
          [sg.Text('Perekonnanimi: ')],
          [sg.InputText(key="perekonnanimi")],
          [sg.Text('_' * 80)],
          [sg.Submit('Graafik'), sg.Submit('Sektordiagramm'), sg.Submit('Tulpdiagramm'),  sg.Cancel('Välju')]] #sg.Submit('Sektordiagramm')
aken = sg.Window('Sinu andmed', paigutus, size=(400,200))
while True:
    syndmus, v22rtused = aken.read()
    #kui aken pannakse kinni, lõpetab programm töö
    if syndmus == sg.WIN_CLOSED or syndmus == 'Välju':
        break
    #kui vajutatakse nuppu 'Järgmine', pannakse põhiaken kinni ja avaneb uus aken
    
    
    #GRAAAAAAAAAFIIIIIIIIIKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
    if syndmus == 'Graafik':
        aken.close()
        
        #salvestame ees- ja perekonnanime muutujatesse
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
        #loome uue paigutuse uue akna jaoks
        #kasutame erinevaid elemente
        paigutus2 = [[sg.Text('Sisesta graafiku andmed', text_color='black', font=("Helvetica", 12))],
                  
                  [sg.Text('Sisesta graafiku x- ja y-telje nimetused (eralda komadega): ')],
                  [sg.InputText(key="graafiknimi")],
                  [sg.Text('Sisesta x väärtused (eralda semikoolonitega): ')],
                  [sg.InputText(key="xgraafikvaartus")],
                  [sg.Text('Sisesta y väärtused (eralda semikoolonitega): ')],
                  [sg.InputText(key="ygraafikvaartus")],
                  [sg.Text('Hoia meeles, et pead sisestama andmed õiges järjekorras. ', text_color='red', font=("helvetica", 10))],
                  [sg.Text('_' * 80)],
                  [sg.Submit('Salvesta'), sg.Cancel('Välju')]]
   
        aken = sg.Window('Vajalikud andmed', paigutus2, size=(400,275))
        syndmus2, v22rtused2 = aken.read()
        
        graafiknimi = v22rtused2['graafiknimi']
        xgraafikvaartus = v22rtused2['xgraafikvaartus']
        ygraafikvaartus = v22rtused2['ygraafikvaartus']
        
        #Muudame nimekirja muutujateks
        a = graafiknimi.split(", ")
#         print(a)
        b = xgraafikvaartus.split("; ")
#         print(b)
        c = ygraafikvaartus.split("; ")
#         print(c)


        bint = list(map(int, b))
        cint = list(map(int, c))
        #akna sulgemisel lõpetab programm töö
        if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Välju':
            break
        
        #kui vajutatakse nuppu 'Salvesta', joonestatakse graafik
        if syndmus2 == 'Salvesta':
             plt.plot(bint, cint)
             
            
             plt.xlabel(a[0])
             plt.ylabel(a[1])
             plt.show()
 
            
            
            
            
            
            
            #TULPDIAGRAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    if syndmus == 'Tulpdiagramm':
        aken.close()        
         
        #Esimese lehe salvestamine 
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
        
        #Uus aken
        paigutus3 = [[sg.Text('Sisesta tulpdiagrammi andmed', text_color='black', font=("Helvetica", 12))],
                  [sg.Text('Sisesta tulpdiagrammi pealkiri: ')],
                  [sg.InputText(key="pealkiritulp")],
                  [sg.Text('Sisesta telgede nimetused (eralda komadega): ')],
                  [sg.InputText(key="nimetused")],
                  [sg.Text('Sisesta tulpade nimetused (eralda komadega): ')],
                  [sg.InputText(key="tulpnimi")],
                  [sg.Text('Sisesta väärtused (eralda semikoolonitega): ')],
                  [sg.InputText(key="väärtused")],
                  [sg.Text('Hoia meeles, et pead sisestama andmed õiges järjekorras. ', text_color='red', font=("helvetica", 10))],
                  [sg.Text('_' * 80)],
                  [sg.Submit('Salvesta'), sg.Cancel('Välju')]]
        
        aken = sg.Window('Vajalikud andmed', paigutus3, size=(600,380))
        syndmus2, v22rtused2 = aken.read()
            
        #salvestame väärtused ja nimetused muutujatesse
        nimetused = v22rtused2['nimetused']
        väärtused = v22rtused2['väärtused']
        pealkiritulp = v22rtused2['pealkiritulp']
        tulpnimi = v22rtused2['tulpnimi']
        
        #Muudame listi üksikuteks muutujateks
        a1 = nimetused.split(", ")
        b1 = väärtused.split("; ")
        c1 = tulpnimi.split(", ")
        
        b1int = list(map(int, b1))
        
#         print(a1)
#         print(b1int)
#         print(c1)
        
        #akna sulgemisel lõpetab programm töö
        if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Välju':
            break
        
        if syndmus2 == 'Salvesta':
            fig, ax = plt.subplots()

            x = c1
            numbricounts = b1int
#             print('x', x)
#             print('numbricounts', numbricounts)
            
            bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

            ax.bar(x, numbricounts, color=bar_colors)

            ax.set_ylabel(a1[1])
            ax.set_xlabel(a1[0])
            ax.set_title(pealkiritulp)
            plt.show()
            #print(eesnimi, perekonnanimi)
            #print(nimetused, väärtused, tulbad)
            
            
            
            
            
            #SEKTORDIAGRAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    if syndmus == 'Sektordiagramm':
        aken.close()        
         
        #Esimese lehe salvestamine 
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
        
        #Uus aken
        paigutus4 = [[sg.Text('Sisesta sektordiagrammi andmed', text_color='black', font=("Helvetica", 12))],
                  
                  [sg.Text('Sisesta nimetused (eralda komadega): ')],
                  [sg.InputText(key="sektornimetused")],
                  [sg.Text('Sisesta väärtused (eralda semikoolonitega): ')],
                  [sg.InputText(key="sektorväärtused")],
                  [sg.Text('Hoia meeles, et pead sisestama andmed õiges järjekorras. ', text_color='red', font=("helvetica", 10))],
                  [sg.Text('_' * 80)],
                  [sg.Submit('Salvesta'), sg.Cancel('Välju')]]
        
        aken = sg.Window('Vajalikud andmed', paigutus4, size=(400,285))
        syndmus3, v22rtused3 = aken.read()
        
        sektornimetused = v22rtused3['sektornimetused']
        sektorväärtused = v22rtused3['sektorväärtused']
        
        
        
        a2 = sektornimetused.split(", ")
        b2 = sektorväärtused.split("; ")
        
        b2int = list(map(int, b2))
        
         #akna sulgemisel lõpetab programm töö
        if syndmus3 == sg.WIN_CLOSED or syndmus3 == 'Välju':
            break
        
        #kui vajutatakse nuppu 'Salvesta', pannakse põhiaken kinni ja avaneb uus aken
        if syndmus3 == 'Salvesta':
            y = np.array(b2int)
            mylabels = a2
            mycolors = ["black", "hotpink", "b", "#4CAF50", "green", "orange"]

            plt.pie(y, labels = mylabels, colors = mycolors)
            
            plt.show() 
            
            print(eesnimi, perekonnanimi)
            print(sektornimetused, sektorväärtused)
        
aken.close()