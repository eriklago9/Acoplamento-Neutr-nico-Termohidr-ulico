"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from botcity.core import DesktopBot
import numpy as np
import matplotlib.pyplot as plt 
import os
import time
import pyautogui
import pyperclip
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
  
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *
n=0
def diretorio():
    dirpath = filedialog.askopenfilename(initialdir=r"C:\Program Files\ANSYS Inc\v212\fluent\ntbin\win64")
    return dirpath 

def ubuntu():
    dirpath = filedialog.askopenfilename(initialdir=r"C:\Program Files\WindowsApps\CanonicalGroupLimited.Ubuntu_2004.4.4.0_x64__79rhkp1fndgsc")
    dir_ubuntu = dirpath
    return dir_ubuntu

def det0():
    dirpath = filedialog.askopenfilename(initialdir=r"C:\Users\erikl\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\LocalState\rootfs\home")
    det0_ubuntu = dirpath
    return det0_ubuntu

def iteracao():
    n = entrada.get()
    return int(n)
    
def simulacao():

    class Bot(DesktopBot):
        def action(self, execution=None):
            # Uncomment to silence Maestro errors when disconnected
            # if self.maestro:
            #     self.maestro.RAISE_NOT_CONNECTED = False

            # Fetch the Activity ID from the task:
            # task = self.maestro.get_task(execution.task_id)
            # activity_id = task.activity_idcd reactor
            
#Exclusão dos Arquivos de Saída da Simulação Termohidráulica para Executar uma nova Simulação: 
            n = iteracao()
            messagebox.showinfo('Orientação 1', \
                                    'Entre com o arquivo .cas')
            simulacao_termo = diretorio()[0:100]
            simulacao_termohidraulica = simulacao_termo[0:100]
            caminho_procura = simulacao_termo[0:50]
            termo_procura = 'pin_results'
            termo_procura1 = 'report-press-outlet-rfile'
            termo_procura2 = 'report-temp-inlet-rfile'
            termo_procura3 = 'temp_med_fuel-rfile'
            termo_procura4 = 'temp_med_helio-rfile'
            termo_procura5 = 'temp_med_water-rfile'
            termo_procura6 = 'temp_med_zirlo-rfile'
            for raiz, diretorios, arquivos in os.walk(caminho_procura):
                for arquivos in arquivos:
                    if termo_procura in arquivos: 
                        os.remove(caminho_procura+"\\pin_results.dat.h5")
                    if termo_procura1 in arquivos:
                        os.remove(caminho_procura+"\\report-press-outlet-rfile.out")
                    if termo_procura2 in arquivos:  
                        os.remove(caminho_procura+"\\report-temp-inlet-rfile.out")
                    if termo_procura3 in arquivos: 
                        os.remove(caminho_procura+"\\temp_med_fuel-rfile.out")
                    if termo_procura4 in arquivos: 
                        os.remove(caminho_procura+"\\temp_med_helio-rfile.out")
                    if termo_procura5 in arquivos:
                        os.remove(caminho_procura+"\\temp_med_water-rfile.out")
                    if termo_procura6 in arquivos:
                        os.remove(caminho_procura+"\\temp_med_zirlo-rfile.out")
#Execução da Simulação Neutrônica:
            messagebox.showinfo('Orientação 2', \
                                    'Insira o arquivo executável do Ubuntu para iniciar a Simulação Neutrônica')
            num_iteracao["text"] = "Iteração nº: 1"
            status_simulacao["background"] = "red"
            status_simulacao["text"] = "Simulação Neutrônica em Andamento"
            v_ubuntu = ubuntu()[0:100]
            var_ubuntu = v_ubuntu[0:100]
            self.execute(var_ubuntu)
            if not self.find( "clickUbuntu", matching=0.97, waiting_time=27000000):
                self.not_found("clickUbuntu")
            self.click()
            self.kb_type("cd reactor")
            self.enter()
            self.kb_type("chmod 777 -R pin")
            self.enter()
            self.kb_type("dos2unix pin")
            self.enter()
            self.kb_type("sss2 pin")
            self.enter()
            if not self.find( "end_simulation_neutronic", matching=0.97, waiting_time=27000000):
                self.not_found("end_simulation_neutronic")
            self.click()
            self.kb_type("exit")
            self.enter()     
#Geração da Potência de ordem 6:
            messagebox.showinfo('Orientação 3', \
                                'Insira o arquivo .det0 para produzir a expressão de ordem 6')
            v_det0 = det0()[0:1000]
            var_det0 = v_det0[0:1000]
            with open(var_det0) as arquivo:
                V: float = (3.141592654*0.0004096*0.0004096*2.4)
                P = []
                linhas = arquivo.readlines()
            for l in range(2,102,1):
                string = (linhas[l])
                valor = (string[52:63])
                y = float(valor)/V
                P.append(y)          
            x = [0.024, 0.048, 0.072, 0.096, 0.12, 0.144, 0.168, 0.192, 0.216, 0.24, 0.264, 0.288, 0.312, 0.336, 0.36,
                0.384, 0.408, 0.432, 0.456, 0.48, 0.504, 0.528, 0.552, 0.576, 0.6, 0.624, 0.648, 0.672, 0.696, 0.72,
                0.744, 0.768, 0.792, 0.816, 0.84, 0.864, 0.888, 0.912, 0.936, 0.96, 0.984, 1.008, 1.032, 1.056, 1.08,
                1.104, 1.128, 1.152, 1.176, 1.2, 1.224, 1.248, 1.272, 1.296, 1.32, 1.344, 1.368, 1.392, 1.416, 1.44,
                1.464, 1.488, 1.512, 1.536, 1.56, 1.584, 1.608, 1.632, 1.656, 1.68, 1.704, 1.728, 1.752, 1.776, 1.8,
                1.824, 1.848, 1.872, 1.896, 1.92, 1.944, 1.968, 1.992, 2.016, 2.04, 2.064, 2.088, 2.112, 2.136, 2.16,
                2.184, 2.208, 2.232, 2.256, 2.28, 2.304, 2.328, 2.352, 2.376, 2.4]
            mod_linear = np.polyfit(x,P,6)
            parcela1 = str(mod_linear[0])
            parcela2 = str(mod_linear[1])
            parcela3 = str(mod_linear[2])
            parcela4 = str(mod_linear[3])
            parcela5 = str(mod_linear[4])
            parcela6 = str(mod_linear[5])
            parcela7 = str(mod_linear[6]) 
            if(mod_linear[0]>0):
                parcela1 = "+"+parcela1[0:14]
            else:
                parcela1 = parcela1[0:15]
            if(mod_linear[1]>0):
                parcela2 = "+"+parcela2[0:14]
            else:
                parcela2 = parcela2[0:15]
            if(mod_linear[2]>0):
                parcela3 = "+"+parcela3[0:14]
            else:
                parcela3 = parcela3[0:15]
            if(mod_linear[3]>0):
                parcela4 = "+"+parcela4[0:14]
            else:
                parcela4 = parcela4[0:15]
            if(mod_linear[4]>0):
                parcela5 = "+"+parcela5[0:14]
            else:
                parcela5 = parcela5[0:15]
            if(mod_linear[5]>0):
                parcela6 = "+"+parcela6[0:14]
            else:
                parcela6 = parcela6[0:15]
            if(mod_linear[6]>0):
                parcela7 = "+"+parcela7[0:14]
            else:
                parcela7 = parcela7[0:15]  
            Pot =(parcela1+"[W m^-9]*z^6"+parcela2+"[W m^-8]*z^5"+parcela3+"[W m^-7]*z^4"+parcela4+"[W m^-6]*z^3"+parcela5+"[W m^-5]*z^2"+parcela6+"[W m^-4]*z"+parcela7+"[W m^-3]")
            Pot_legenda = (parcela1+"z^6"+parcela2+"z^5"+parcela3+"z^4"+parcela4+"z^3"+parcela5+"z^2"+parcela6+"z"+parcela7)
            texto_potencia["text"] = Pot
            print(Pot)
            fig, ax = plt.subplots(figsize = (10, 5)) 
            plt.title('Distribuição de Potência (W/m)')
            ax.set_xlabel('Z(m)\n'+Pot_legenda, color = 'r')
            ax.set_ylabel('Potência(W)', color = 'r') 
            ax.plot(x, P, "go", color = 'g')
            ax.plot(x, P, color = 'r')
            plt.show()
            pyperclip.copy(Pot)
            status_simulacao["background"] = "green"
            status_simulacao["text"] = "Simulação Neutrônica Finalizada"
#Atribuição da Potência ao Arquivo .cas.h5:
            self.execute(simulacao_termohidraulica)
            if not self.find( "select_pot", matching=0.97, waiting_time=10000):
                self.not_found("select_pot")
            self.click()
            for a in range(8):
                pyautogui.press('right')
            for b in range(183):
                pyautogui.press('delete')
            pyautogui.hotkey('ctrl', 'v')
            for c in range(237):
                pyautogui.press('left')
            pyautogui.hotkey('ctrl', 's')
            time.sleep(5)
            pyautogui.hotkey('alt', 'f4')
#Execução da Simulação Termohidráulica: 
            status_simulacao["background"] = "red"
            status_simulacao["text"] = "Sim. Termohidráulica em Andamento"
            os.startfile("cmd")
            if not self.find( "select_CFD", matching=0.97, waiting_time=10000):
                self.not_found("select_CFD")
            self.click()
            self.kb_type("cd /d C:\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64")
            self.enter()
            if not self.find( "executeCFD", matching=0.97, waiting_time=10000):
                self.not_found("executeCFD")
            self.click()
            self.kb_type("fluent 3ddp -g -t4 -i pin")
            self.enter()
            if not self.find( "exit_fluent", matching=0.97, waiting_time=7200000):
                self.not_found("exit_fluent")
            self.click()
            self.kb_type("exit")
            self.enter()
            status_simulacao["background"] = "green"
            status_simulacao["text"] = "Sim. Termohidráulica Finalizada"
#Substituição das Temperaturas no Arquivo pin em Serpent: 
            with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_fuel-rfile.out') as arquivo:
                file_lines = arquivo.readlines()
                arquivo.close()
                last_line = file_lines[len(file_lines) - 1]
                temp_fuel = last_line[4:15]
                texto_fuel["text"] = temp_fuel
                print(temp_fuel)
            with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_helio-rfile.out') as arquivo:
                file_lines = arquivo.readlines()
                arquivo.close()
                last_line = file_lines[len(file_lines) - 1]
                print(last_line[4:15])
            with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_zirlo-rfile.out') as arquivo:
                file_lines = arquivo.readlines()
                arquivo.close()
                last_line = file_lines[len(file_lines) - 1]
                temp_zirlo = last_line[4:15]
                texto_zircaloy["text"] = temp_zirlo
                print(temp_zirlo)
            with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_water-rfile.out') as arquivo:
                file_lines = arquivo.readlines()
                arquivo.close()
                last_line = file_lines[len(file_lines) - 1]
                temp_water = last_line[4:15]
                texto_water["text"] = temp_water
                print(temp_water)
            with open('C:\\Users\\erikl\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\\LocalState\\rootfs\\home\\eslago\\reactor\\pin', 'r', encoding='utf-8') as file:
                data = file.readlines()
                data[3] = "mat fuel     -10.1 vol 126.43 tmp "+temp_fuel+" rgb 255 255 150 burn 1\n"
                data[13] = "mat zirlo -6.56000E+00 vol 170.03 tmp "+temp_zirlo+" rgb 200 200 200\n"
                data[39] = "mat water -0.709 tmp "+temp_water+" moder lwtr 1001 rgb 0 200 255\n"
                data[43] = "therm lwtr "+temp_water+" lwj3.11t lwj3.13t\n"
            with open('C:\\Users\\erikl\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\\LocalState\\rootfs\\home\\eslago\\reactor\\pin', 'w', encoding='utf-8') as file:
                    file.writelines(data) 
#Segunda iteração sem inserção dos diretórios
#Exclusão dos Arquivos de Saída da Simulação Termohidráulica para Executar uma nova Simulação: 
            i=0
            while i<(n-1):
                num_iteracao["text"] = "Iteração nº: "+i+2
                termo_procura = 'pin_results'
                termo_procura1 = 'report-press-outlet-rfile'
                termo_procura2 = 'report-temp-inlet-rfile'
                termo_procura3 = 'temp_med_fuel-rfile'
                termo_procura4 = 'temp_med_helio-rfile'
                termo_procura5 = 'temp_med_water-rfile'
                termo_procura6 = 'temp_med_zirlo-rfile'
                for raiz, diretorios, arquivos in os.walk(caminho_procura):
                    for arquivos in arquivos:
                        if termo_procura in arquivos: 
                            os.remove(caminho_procura+"\\pin_results.dat.h5")
                        if termo_procura1 in arquivos:
                            inicio = open(caminho_procura+'\\report-press-outlet-rfile.out', 'r')
                            inicio.close() 
                            os.remove(caminho_procura+"\\report-press-outlet-rfile.out")
                        if termo_procura2 in arquivos: 
                            inicio = open(caminho_procura+'\\report-temp-inlet-rfile.out', 'r')
                            inicio.close() 
                            os.remove(caminho_procura+"\\report-temp-inlet-rfile.out")
                        if termo_procura3 in arquivos: 
                            inicio = open(caminho_procura+'\\temp_med_fuel-rfile.out', 'r')
                            inicio.close() 
                            os.remove(caminho_procura+"\\temp_med_fuel-rfile.out")
                        if termo_procura4 in arquivos: 
                            inicio = open(caminho_procura+'\\temp_med_helio-rfile.out', 'r')
                            inicio.close()
                            os.remove(caminho_procura+"\\temp_med_helio-rfile.out")
                        if termo_procura5 in arquivos:
                            inicio = open(caminho_procura+'\\temp_med_water-rfile.out', 'r')
                            inicio.close()
                            os.remove(caminho_procura+"\\temp_med_water-rfile.out")
                        if termo_procura6 in arquivos:
                            inicio = open(caminho_procura+'\\temp_med_zirlo-rfile.out', 'r')
                            inicio.close()
                            os.remove(caminho_procura+"\\temp_med_zirlo-rfile.out")
#Execução da Simulação Neutrônica:
                status_simulacao["background"] = "red"
                status_simulacao["text"] = "Simulação Neutrônica em Andamento"
                self.execute(var_ubuntu)
                if not self.find( "clickUbuntu", matching=0.97, waiting_time=27000000):
                    self.not_found("clickUbuntu")
                self.click()
                self.kb_type("cd reactor")
                self.enter()
                self.kb_type("chmod 777 -R pin")
                self.enter()
                self.kb_type("dos2unix pin")
                self.enter()
                self.kb_type("sss2 pin")
                self.enter()
                if not self.find( "end_simulation_neutronic", matching=0.97, waiting_time=27000000):
                    self.not_found("end_simulation_neutronic")
                self.click()
                self.kb_type("exit")
                self.enter()     
#Geração da Potência de ordem 6:
                with open(var_det0) as arquivo:
                    V: float = (3.141592654*0.0004096*0.0004096*2.4)
                    P = []
                    linhas = arquivo.readlines()
                for l in range(2,102,1):
                    string = (linhas[l])
                    valor = (string[52:63])
                    y = float(valor)/V
                    P.append(y)          
                x = [0.024, 0.048, 0.072, 0.096, 0.12, 0.144, 0.168, 0.192, 0.216, 0.24, 0.264, 0.288, 0.312, 0.336, 0.36,
                    0.384, 0.408, 0.432, 0.456, 0.48, 0.504, 0.528, 0.552, 0.576, 0.6, 0.624, 0.648, 0.672, 0.696, 0.72,
                    0.744, 0.768, 0.792, 0.816, 0.84, 0.864, 0.888, 0.912, 0.936, 0.96, 0.984, 1.008, 1.032, 1.056, 1.08,
                    1.104, 1.128, 1.152, 1.176, 1.2, 1.224, 1.248, 1.272, 1.296, 1.32, 1.344, 1.368, 1.392, 1.416, 1.44,
                    1.464, 1.488, 1.512, 1.536, 1.56, 1.584, 1.608, 1.632, 1.656, 1.68, 1.704, 1.728, 1.752, 1.776, 1.8,
                    1.824, 1.848, 1.872, 1.896, 1.92, 1.944, 1.968, 1.992, 2.016, 2.04, 2.064, 2.088, 2.112, 2.136, 2.16,
                    2.184, 2.208, 2.232, 2.256, 2.28, 2.304, 2.328, 2.352, 2.376, 2.4]
                mod_linear = np.polyfit(x,P,6)
                parcela1 = str(mod_linear[0])
                parcela2 = str(mod_linear[1])
                parcela3 = str(mod_linear[2])
                parcela4 = str(mod_linear[3])
                parcela5 = str(mod_linear[4])
                parcela6 = str(mod_linear[5])
                parcela7 = str(mod_linear[6]) 
                if(mod_linear[0]>0):
                    parcela1 = "+"+parcela1[0:14]
                else:
                    parcela1 = parcela1[0:15]
                if(mod_linear[1]>0):
                    parcela2 = "+"+parcela2[0:14]
                else:
                    parcela2 = parcela2[0:15]
                if(mod_linear[2]>0):
                    parcela3 = "+"+parcela3[0:14]
                else:
                    parcela3 = parcela3[0:15]
                if(mod_linear[3]>0):
                    parcela4 = "+"+parcela4[0:14]
                else:
                    parcela4 = parcela4[0:15]
                if(mod_linear[4]>0):
                    parcela5 = "+"+parcela5[0:14]
                else:
                    parcela5 = parcela5[0:15]
                if(mod_linear[5]>0):
                    parcela6 = "+"+parcela6[0:14]
                else:
                    parcela6 = parcela6[0:15]
                if(mod_linear[6]>0):
                    parcela7 = "+"+parcela7[0:14]
                else:
                    parcela7 = parcela7[0:15]  
                Pot =(parcela1+"[W m^-9]*z^6"+parcela2+"[W m^-8]*z^5"+parcela3+"[W m^-7]*z^4"+parcela4+"[W m^-6]*z^3"+parcela5+"[W m^-5]*z^2"+parcela6+"[W m^-4]*z"+parcela7+"[W m^-3]")
                Pot_legenda = (parcela1+"z^6"+parcela2+"z^5"+parcela3+"z^4"+parcela4+"z^3"+parcela5+"z^2"+parcela6+"z"+parcela7)
                texto_potencia["text"] = Pot
                print(Pot)
                fig, ax = plt.subplots(figsize = (10, 5)) 
                plt.title('Distribuição de Potência (W/m)')
                ax.set_xlabel('Z(m)\n'+Pot_legenda, color = 'r')
                ax.set_ylabel('Potência(W)', color = 'r') 
                ax.plot(x, P, "go", color = 'g')
                ax.plot(x, P, color = 'r')
                plt.show()
                pyperclip.copy(Pot)
                status_simulacao["background"] = "green"
                status_simulacao["text"] = "Simulação Neutrônica Finalizada"
#Atribuição da Potência ao Arquivo .cas.h5:
                self.execute(simulacao_termohidraulica)
                if not self.find( "select_pot", matching=0.97, waiting_time=10000):
                    self.not_found("select_pot")
                self.click()
                for a in range(8):
                    pyautogui.press('right')
                for b in range(183):
                    pyautogui.press('delete')
                pyautogui.hotkey('ctrl', 'v')
                for c in range(237):
                    pyautogui.press('left')
                pyautogui.hotkey('ctrl', 's')
                time.sleep(5)
                pyautogui.hotkey('alt', 'f4')
#Execução da Simulação Termohidráulica: 
                status_simulacao["background"] = "red"
                status_simulacao["text"] = "Sim. Termohidráulica em Andamento"
                os.startfile("cmd")
                if not self.find( "select_CFD", matching=0.97, waiting_time=10000):
                    self.not_found("select_CFD")
                self.click()
                self.kb_type("cd /d C:\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64")
                self.enter()
                if not self.find( "executeCFD", matching=0.97, waiting_time=10000):
                    self.not_found("executeCFD")
                self.click()
                self.kb_type("fluent 3ddp -g -t4 -i pin")
                self.enter()
                if not self.find( "exit_fluent", matching=0.97, waiting_time=7200000):
                    self.not_found("exit_fluent")
                self.click()
                self.kb_type("exit")
                self.enter()
                status_simulacao["background"] = "green"
                status_simulacao["text"] = "Sim. Termohidráulica Finalizada"
#Substituição das Temperaturas no Arquivo pin em Serpent: 
                with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_fuel-rfile.out') as arquivo:
                    file_lines = arquivo.readlines()
                    arquivo.close()
                    last_line = file_lines[len(file_lines) - 1]
                    temp_fuel = last_line[4:15]
                    texto_fuel["text"] = temp_fuel
                    print(temp_fuel)
                with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_helio-rfile.out') as arquivo:
                    file_lines = arquivo.readlines()
                    arquivo.close()
                    last_line = file_lines[len(file_lines) - 1]
                    print(last_line[4:15])
                with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_zirlo-rfile.out') as arquivo:
                    file_lines = arquivo.readlines()
                    arquivo.close()
                    last_line = file_lines[len(file_lines) - 1]
                    temp_zirlo = last_line[4:15]
                    texto_zircaloy["text"] = temp_zirlo
                    print(temp_zirlo)
                with open(r'C:\\Program Files\ANSYS Inc\\v212\\fluent\\ntbin\win64\\temp_med_water-rfile.out') as arquivo:
                    file_lines = arquivo.readlines()
                    arquivo.close()
                    last_line = file_lines[len(file_lines) - 1]
                    temp_water = last_line[4:15]
                    texto_water["text"] = temp_water
                    print(temp_water)
                with open('C:\\Users\\erikl\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\\LocalState\\rootfs\\home\\eslago\\reactor\\pin', 'r', encoding='utf-8') as file:
                    data = file.readlines()
                    data[3] = "mat fuel     -10.1 vol 126.43 tmp "+temp_fuel+" rgb 255 255 150 burn 1\n"
                    data[13] = "mat zirlo -6.56000E+00 vol 170.03 tmp "+temp_zirlo+" rgb 200 200 200\n"
                    data[39] = "mat water -0.709 tmp "+temp_water+" moder lwtr 1001 rgb 0 200 255\n"
                    data[43] = "therm lwtr "+temp_water+" lwj3.11t lwj3.13t\n"
                with open('C:\\Users\\erikl\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu_79rhkp1fndgsc\\LocalState\\rootfs\\home\\eslago\\reactor\\pin', 'w', encoding='utf-8') as file:
                        file.writelines(data)
                i+=1   
                # Uncomment to mark this task as finished on BotMaestro
                # self.maestro.finish_task(
                #     task_id=execution.task_id,
                #     status=AutomationTaskFinishStatus.SUCCESS,
                #     message="Task Finished OK."
                # )

        def not_found(self, label):
            print(f"Element not found: {label}")

    if __name__ == '__main__':
        Bot.main()

janela = Tk()
janela.title("Acoplamento Neutrônico-Termohidráulico PPGMC")
janela.geometry("580x600") 
janela.minsize(1366, 768) 
janela.maxsize(1366, 768)

image=PhotoImage(file=".\\resources\\reator_ipwr.png")
image=image.subsample(1,1)
labelimage=Label(image=image)
labelimage.place(x=0,y=0, relwidth=1.0, relheight=1.0)

texto_orientacao = Label(janela, text="ACOPLAMENTO NEUTRÔNICO-TERMOHIDRÁULICO - PPGMC", font="Arial 14", bd=1, relief="solid") 
texto_orientacao.grid(column=0, row=0, padx=400, pady=10)

texto_orientacao0 = Label(janela, text="Digite o número de iterações desejado:", font="Calibri 12")
texto_orientacao0.grid(column=0, row=1, padx=10, pady=10)

entrada = Entry(janela)
entrada.grid(column=0, row=2, padx=10, pady=10)

botao1 = Button(janela, text="Confirmar", command = iteracao, font="Calibri 12")
botao1.grid(column=0, row=3, padx=10, pady=10)

botao = Button(janela, text="Clique para iniciar a simulação", command=simulacao, font="Calibri 12")
botao.grid(column=0, row=4, padx=10, pady=10)

texto_orientacao2 = Label(janela, text="Distribuição de Potência(W/m³):", font="Calibri 12")
texto_orientacao2.grid(column=0, row=5, padx=10, pady=10)

texto_potencia = Label(janela, text='')
texto_potencia.grid(column=0, row=6, padx=10, pady=10)

texto_orientacao3 = Label(janela, text="Temperatura da Água(K):", font="Calibri 12")
texto_orientacao3.grid(column=0, row=7, padx=10, pady=10)

texto_water = Label(janela, text='')
texto_water.grid(column=0, row=8, padx=10, pady=10)

texto_orientacao4 = Label(janela, text="Temperatura do Zircaloy(K):", font="Calibri 12")
texto_orientacao4.grid(column=0, row=9, padx=10, pady=10)

texto_zircaloy = Label(janela, text='')
texto_zircaloy.grid(column=0, row=10, padx=10, pady=10)

texto_orientacao5 = Label(janela, text="Temperatura do UO2(K):", font="Calibri 12")
texto_orientacao5.grid(column=0, row=11, padx=10, pady=10)

texto_fuel = Label(janela, text='', font="Calibri 12")
texto_fuel.grid(column=0, row=12, padx=10, pady=10)


num_iteracao = Label(janela, text='', font="Calibri 12")
num_iteracao.grid(column=0, row=13, padx=10, pady=10)

status_simulacao = Label(janela, text='', font="Calibri 12")
status_simulacao.grid(column=0, row=14, padx=10, pady=10)


janela.mainloop()






