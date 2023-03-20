from ursina import *
from motor import *
from window_panel import WindowPanelM
from math import sqrt
from MEditorCamera import  MEditorCamera


app = Ursina(borderless=True)
window.fps_counter.enabled = False
window.title = 'Motor'

class Menu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.main_menu = Entity(parent = self, enabled = True)
        self.obj_menu = Entity(parent = self, enabled = False)
        self.calc_menu = Entity(parent = self, enabled = False)
        self.cred_menu = Entity(parent = self, enabled = False)
        self.models = Models(add_to_scene_entitites = False, enabled = False)
        
        self.main()
        self.camera = MEditorCamera(enabled = False)
        self.camera.rotate_around_entity = True

        self.models.motor_aberto()
        self.models.motor_fechado()


    def main(self):
        self.calculos()
        self.modelos()

        b3 = Button(text='Simular Modelos', x=0, y =.2, scale_x=.5, scale_y=.09, parent = self.main_menu)
        b3.on_click = lambda:obj_view()

        b2 = Button(text='Simular Valores', x=.0, y=.05, scale_x=.5, scale_y=.09, parent=self.main_menu)
        b2.on_click = lambda:calculos()

        b4 = Button(text='Créditos', x=0, y =-.1, scale_x=.5, scale_y=.09, parent = self.main_menu)
        b4.on_click = lambda:creditos()

        def obj_view():
            self.main_menu.disable()
            self.obj_menu.enable()
            self.exit_text()
            self.models.enable()
            self.camera.enable()

        def calculos():
            self.main_menu.disable()
            self.calc_menu.enable()
            self.exit_text()

        def creditos():
            self.main_menu.disable()
            self.cred_menu.enable()
            self.exit_text()

    def modelos(self):
        Panel(model= Quad(radius = .015), y = -.705, scale = (1.25, .62), parent = self.obj_menu)
        objView_Button = ButtonGroup(('Motor Fechado', 'Motor Aberto', 'Eixo', 'Estator', 'Rotor'), 
        default = 'Motor Fechado', x= -.595, y=-.42, scale = (.06, .06), parent = self.obj_menu)
        breakObj_Button = ButtonGroup(('off', 'on'), min_selection=1, selected_color = color.red, 
        scale=(.07, .065), position = (-.81, -.42), parent = self.obj_menu)


        def on_disable():
            objView_Button.value = 'Motor Fechado'
            self.models.disable()
            breakObj_Button.value = 'off'
            self.camera.disable()
            self.camera.animate_position(self.camera.start_position)
        self.obj_menu.on_disable = on_disable


        def on_value_changed():
            if objView_Button.value == 'Motor Fechado':
                self.models.objViewer('M_fechado')
                breakObj_Button.visible = True
            else:
                if objView_Button.value == 'Motor Aberto':
                    self.models.objViewer('M_aberto')
                elif objView_Button.value == 'Eixo':
                    self.models.objViewer('Eixo')
                elif objView_Button.value == 'Estator':
                    self.models.objViewer('Estator')
                elif objView_Button.value == 'Rotor':
                    self.models.objViewer('Rotor')
                breakObj_Button.visible = False
                breakObj_Button.value = 'off'
            self.camera.animate_position(self.camera.start_position)
        objView_Button.on_value_changed = on_value_changed

        def on_value_changed():
            if breakObj_Button.value == 'off':
                breakObj_Button.selected_color = color.green
                self.models.assembleObj()
            else:
                breakObj_Button.selected_color = color.red
                self.models.breakObj()
        breakObj_Button.on_value_changed = on_value_changed


    def calculos(self):
        Text(text = 'Rendimento:', x=.02, y=0, color=color.black, parent = self.calc_menu)
        inp_rend = InputField(x=.15, y=-.05, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)

        Text(text = 'Quantidade de polos:', x=-.28, y=0, color=color.black, parent = self.calc_menu)
        inp_polos = InputField(x=-.15, y=-.05, next_field=inp_rend, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)

        Text(text = 'Velocidade Medida no Rotor:', x=.02, y=.1, color=color.black, parent = self.calc_menu)
        inp_rpm = InputField(x=.15, y=.05, next_field=inp_polos, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)

        Text(text = 'Relação (In/Ip):', x=-.28, y=.1, color=color.black, parent = self.calc_menu)
        inp_Ir = InputField(x=-.15, y=.05, next_field=inp_rpm, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)

        Text(text = 'Fator de Potência:', x=.02, y=.2, color=color.black, parent = self.calc_menu)
        inp_fu = InputField(x=.15, y=.15, next_field=inp_Ir, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)

        Text(text = 'Corrente Nominal:', x=-.28, y=.2, color=color.black, parent = self.calc_menu)
        inp_in = InputField(x=-.15, y=.15, next_field=inp_fu, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)

        Text(text = 'Frequência:',x=.02, y=.3, color=color.black, parent = self.calc_menu)
        inp_fhz = InputField(x=.15, y=.25, next_field=inp_in, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)

        Text(text = 'Tensão Nominal:', x=-.28, y=.3, color=color.black, parent = self.calc_menu)
        inp_vn = InputField(x=-.15, y=.25, next_field=inp_fhz, limit_content_to='1234567890.', scale_x=.25, parent = self.calc_menu)
        inp_rend.next_field = inp_vn

        cred_text = '                           CRÉDITOS: \n\n\nDISCENTE MÉDIO INTEGRADO: \n\n- RENNAN MAGALHÃES\n- PHILLIPE ANTÔNIO FERREIRA\n\n\nDISCENTE DE ENGENHARIA:\n\n- NATHAN MACIEL\n- CASSIANO MELO \n- LUÍS MAGALHÃES\n\n\nDOCENTE ORIENTADOR: \n\n- MARCONNI FREITAS BARROSO'
        self.cred_text = Text(text = cred_text, position=(-.25,.2), background=True, parent = self.cred_menu)

        inp_vn.tooltip = Tooltip("[SI] = V")
        inp_in.tooltip = Tooltip("[SI] = A")
        inp_rpm.tooltip = Tooltip("[SI] = RPM")
        inp_fhz.tooltip = Tooltip("[SI] = HZ")
        inp_rend.tooltip = Tooltip("%")
        inp_polos.tooltip = Tooltip("Pares")


        b1 = Button(text='Calcular', x = 0, y = -.2, scale_x=.2, scale_y=.07, parent=self.calc_menu)
        b1.on_click = lambda:Calcular()


        error_text = Text(text='Limite de Resultados atingido,\nfeche uma janela e tente novamente.', 
        size = Text.size, position = (-.215, -.35), background = True, enabled = False)
        error_input = Text(text="Erro: Os espaços não podem estar vazios!!\nPreencha todos os dados.", 
        size = Text.size, y = -.35, origin = (0,0), background=True, enabled = False)
        wp_S_coord={0:[0,(-.6, .47)], 1:[0,(.6, .47)], 2:[0,(-.6, .15)], 3:[0,(.6, .15)], 4:[0,(-.6, -.17)], 5:[0,(.6, -.17)]}


        '''Linhas de chamada
        line = Panel(model = 'line', rotation = (0,0,90))
        line = Panel(model = 'line', scale_x = 1000)
        '''

        def on_disable():
            error_text.disable()
            error_input.disable()
        self.calc_menu.on_disable = on_disable

        def show_Res(resultados):
            def subtract():
                wp_S.close()
                wp_S_coord[num][0] = 0
                error_text.disable()
            for num in wp_S_coord:
                if wp_S_coord[num][0] == 0:
                    wp_S_coord[num][0] = 1
                    wp_S = WindowPanelM(
                        title='Resultado ' + str(num+1),
                        content=(
                            Text(resultados),
                            Button(text='x', scale=(.05, .025), on_click = lambda:subtract(), 
                                rounded = .05, color = color.red.tint(-.2), tipo='exit')
                        ),
                        popup = False,
                        enabled = True,
                        position = wp_S_coord[num][1],
                        parent = self.calc_menu
                    )
                    wp_S.panel.scale_y = 5
                    break
            else:
                if error_input.enabled == True:
                    error_input.disable()
                error_text.enable()

        def Calcular():
            if (inp_vn.text == '0' or inp_in.text == '0' or inp_fhz.text == '0' or inp_rpm.text == '0' or inp_fu.text == '0' or inp_polos.text == '0' or inp_Ir.text == '0' or inp_rend.text == '0'):
                error_input.text = 'ERRO! Os valores de entrada\n não podem ser iguais a zero.'
                error_input.background = True
                error_input.enable()
                error_text.disable()
            else:
                try:
                    Vn = float(inp_vn.text)
                    In = float(inp_in.text)
                    fhz = float(inp_fhz.text)
                    rpm_med = float(inp_rpm.text)
                    cosp = float(inp_fu.text)
                    Polos = float(inp_polos.text)
                    Ir = float(inp_Ir.text) #Ir = Ip/In
                    rend = float(inp_rend.text)
                    Ip = Ir * In
                    vel_rotor = (fhz * 120)/(Polos)  
                    esc = ((vel_rotor - rpm_med)/(vel_rotor))*100
                    Potencia = Vn*In*cosp*sqrt(3)*rend
                    Potenciacv = Potencia/746
                    show_Res(f"\n{'Potência (W):       ':} {Potencia:.0f} W\n\
    {'Corrente de partida:       ':} {Ip:.2f} A\n\
    {'Velocidade no rotor:       ':} {vel_rotor:.2f} RPM\n\
    {'Escorregamento:       ':} {esc:.2f} %\n\
    {'Potência (CV):         ':} {Potenciacv:.2f} CV")
                    error_input.disable()
                except ValueError:
                    if error_text.enabled == True:
                        error_text.disable()
                    error_input.text = "Erro: Os espaços não podem estar vazios!!\nPreencha todos os dados."
                    error_input.background = True
                    error_input.enable()

    def input(self, key):
        if key == "escape":
            if self.obj_menu.enabled:
                self.obj_menu.disable()
            elif self.calc_menu.enabled:            
                self.calc_menu.disable()
            elif self.cred_menu.enabled:            
                self.cred_menu.disable()
            destroy(self.text_exit)
            self.main_menu.enable()
        if key == "left mouse up" and self.obj_menu.enabled:
            if self.models.m_aberto.enabled:
                self.camera.get_pos = self.models.m_aberto.position
            elif self.models.m_fechado.enabled:
                self.camera.get_pos = self.models.m_fechado.position 


    def exit_text(self):
        self.text_exit = Text(text='Pressione "Esc" para sair', position=(-.15, .42), background=True)
        destroy(self.text_exit, delay=5)

menu = Menu()

app.run()