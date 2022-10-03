import PySimpleGUI as sg
import os
from datetime import date
#funktsioon hetkevanuse arvutamiseks
def arvuta_vanus(sünnipäev):
    täna = date.today()
    vanus = täna.year - sünnipäev.year - ((täna.month, täna.day) < (sünnipäev.month, sünnipäev.day))
    return vanus
sg.theme('Purple')
paigutus = [[sg.Text('Andmed', text_color='black', font=("Helvetica", 12))],
          [sg.Text('Insert dick: ')],
          [sg.InputText(key="eesnimi")],
          [sg.Text('Sisesta väärtus: ')],
          [sg.InputText(key="perekonnanimi")],
        
          [sg.Text('_' * 80)],
          [sg.Submit('Järgmine'), sg.Cancel('Välju')]]
aken = sg.Window('1. aken: nimi', paigutus, size=(600,400))
while True:
    syndmus, v22rtused = aken.read()
    #kui aken pannakse kinni, lõpetab programm töö
    if syndmus == sg.WIN_CLOSED or syndmus == 'Sulge aken':
        break
    #kui vajutatakse nuppu 'Järgmine', pannakse põhiaken kinni ja avaneb uus aken
    if syndmus == 'Järgmine':
        aken.close()
        
        #salvestame ees- ja perekonnanime muutujatesse
        eesnimi = v22rtused['eesnimi']
        perekonnanimi = v22rtused['perekonnanimi']
        
       
        
        #loome uue paigutuse uue akna jaoks
        #kasutame erinevaid elemente
        paigutus2 = [[sg.Text('Sisesta tervitatava sünnipäev, -kuu ja -aasta!', text_color='black', font=("Helvetica", 12))],
                  [sg.Text('Päev: ', size=(10,1)), sg.Slider(range=(1,31), orientation='h', size=(50,25), key='päev')],
                  [sg.Text('Kuu: ', size=(10,1)), sg.Listbox(values=('jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november', 'detsember'), key='kuu', size=(10, 6))],
                  [sg.Text('Aasta: ', size=(10,1)), sg.InputCombo(('1995', '1996', '1997', '1998', '1999', '2000'), size=(5,10), key='aasta')],
                  [sg.Text('_' * 80)],
                  [sg.Text('Vali tervituspilt: '), sg.Input(size=(20,1)), sg.FileBrowse('Sirvi', key='sirvitud_fail')],
                  [sg.Submit('Sisesta'), sg.Cancel('Välju')]]
   
        aken = sg.Window('2. aken: sünnipäev', paigutus2, size=(600,400))
        syndmus2, v22rtused2 = aken.read()
        
        #akna sulgemisel lõpetab programm töö
        if syndmus2 == sg.WIN_CLOSED or syndmus2 == 'Välju':
            break
        
        #kui vajutatakse nuppu 'Sisesta', pannakse põhiaken kinni ja avaneb uus aken
        if syndmus2 == 'Sisesta':
            aken.close()
            
            #salvestame sünnikuupäeva detailid muutujatesse
            päev = int(v22rtused2['päev'])
            kuu = v22rtused2['kuu'][0]
            aasta = int(v22rtused2['aasta'])
            
            #vastavalt kuule leiame selle kuu "järjekorranumbri", mida kasutame funktsioonis            
            if kuu == 'jaanuar':
                kuu2 = 1
            if kuu == 'veebruar':
                kuu2 = 2
            if kuu == 'märts':
                kuu2 = 3
            if kuu == 'aprill':
                kuu2 = 4
            if kuu == 'mai':
                kuu2 = 5
            if kuu == 'juuni':
                kuu2 = 6
            if kuu == 'juuli':
                kuu2 = 7
            if kuu == 'august':
                kuu2 = 8
            if kuu == 'september':
                kuu2 = 9
            if kuu == 'oktoober':
                kuu2 = 10
            if kuu == 'november':
                kuu2 = 11
            if kuu == 'detsember':
                kuu2 = 12
            
            #funktsioon arvutab hetkevanuse
            #argumendiks määrame kuupäeva kujul (YY,MM,DD) sünnipäeva
            vanus = arvuta_vanus(date(aasta, kuu2, päev))
            
            #failipuust leiame vaid pildifaili nime
            fail = v22rtused2['sirvitud_fail']
            puu, failinimi = os.path.split(fail)
            
            #loome uue paigutuse viimase akna jaoks, kus kuvame kogu informatsiooni            
            paigutus3 = [[sg.Text('Tere, ' + eesnimi + ' ' + perekonnanimi + '! (vanus: ' +  str(vanus) + ' aastat)')],
                       [sg.Text('Sulle on saadetud tervitus: ')],
                       [sg.Image(failinimi)],
                       [sg.Submit('Välju')]]
            
            aken = sg.Window('3. aken: tervituskaart', paigutus3)
            syndmus3, v22rtused3 = aken.read()
            
            #sulgemisel lõpetab programm töö
            if syndmus3 == sg.WIN_CLOSED:
                break
            #nuppu vajutades sulgub põhiaken ning avaneb hüpikaken
            if syndmus3 == 'Välju':
                aken.close()             
                sg.Popup('Aitäh!')
aken.close()