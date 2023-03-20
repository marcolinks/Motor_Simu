from ursina import *
from ursina.shaders import basic_lighting_shader, matcap_shader

class Models(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)

        self.m_aberto = Entity(parent = self, add_to_scene_entities=False, enabled = False, origin = Vec3(0,0,0), position = (0,0,0)) #(0.145,0.386,0.01)
        self.m_fechado = Entity(parent = self, add_to_scene_entities=False, enabled = False, position = (0,0,0))


    def breakObj(self):
        self.MF_dict[0].animate_position((2.4, 0, 0), duration=1)
        #self.MF_dict[1].position = self.MF_dict[3].position = self.MF_dict[12].position = (0,0,0)
        self.MF_dict[2].animate_position((-4.9,0,0), duration = 1)
        self.MF_dict[4].animate_position((1,0,0), duration = 1)
        self.MF_dict[5].animate_position((0,0,2), duration = 1)
        self.MF_dict[6].animate_position((0,0,1.5), duration = 1)
        self.MF_dict[7].animate_position((0,0,.5), duration = 1)
        for i in range(8, 10):
            self.MF_dict[i].animate_position((0,0,1.2), duration = 1)
        self.MF_dict[11].animate_position((0,0,.7), duration = 1)
        self.MF_dict[14].animate_position((-2.3,0,0), duration = 1)
        self.MF_dict[15].animate_position((-2.3,0,0), duration = 1)
        self.MF_dict[16].animate_position((-3.5,0,0), duration = 1)
        self.MF_dict[17].animate_position((1.2,0,0), duration = 1)
        self.MF_dict[18].animate_position((-4,0,0), duration = 1)
        self.MF_dict[19].animate_position((.5,0,0), duration = 1)

    def assembleObj(self):
        for i in range(20):
            if i == 13:
                self.MF_dict[i].animate_position((.33, 0, 0), duration = .5)
            else:
                self.MF_dict[i].animate_position((0,0,0), duration = .5)
    
    def on_enable(self):
        try:
            self.m_fechado.enabled = True
            print ('aaaa')
        except AttributeError:
            print('bbbb')

    def objViewer(self, x):
        if x == 'M_aberto':
            self.m_aberto.enable()
            self.m_fechado.disable()
        else:
            self.m_fechado.enable()
            self.m_aberto.disable()
            if x == 'M_fechado':
                for i in self.MF_dict:
                    if not self.MF_dict[i].enabled:
                        self.MF_dict[i].enable()
            elif x == 'Eixo':
                for i in self.MF_dict:
                    if i > 14:
                        self.MF_dict[i].enable()
                    else:
                        self.MF_dict[i].disable()
            elif x == 'Rotor':
                for i in self.MF_dict:
                    if i == 14:
                        self.MF_dict[i].enable()
                    else:
                        self.MF_dict[i].disable()
            elif x == 'Estator':
                for i in self.MF_dict:
                    if i == 12 or i == 13:
                        self.MF_dict[i].enable()
                    else:
                        self.MF_dict[i].disable()
                        
    
    
    def motor_fechado(self):
        tampaT_carcaca = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Carcaça/A_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        corpo_carcaca = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Carcaça/A_2.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        tampaD_carcaca = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Carcaça/A_3.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        pes_carcaca = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Carcaça/A_4.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        t_dreno = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Carcaça/A_5.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        tampa_terminais = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Caixa_terminais/B_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        molduraT_terminais = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Caixa_terminais/B_2.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/metal_verde.png')


        caixa_terminais = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Caixa_terminais/B_3.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        terminais = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Caixa_terminais/B_4.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/metal_cobre.png')


        QD_terminais = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Caixa_terminais/B_5.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/metal_laranja.png')

        
        cabos_terminais = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Caixa_terminais/B_6.obj', scale = 12, shader = basic_lighting_shader)

        
        painel_terminais = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Caixa_terminais/B_7.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/metal_verde.png')


        corpo_estator = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Estator/C_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_estator.png')

        
        bobinas_estator = Entity(parent = self.m_fechado, x=.33, model = 'assets/Motor_fechado/Estator/C_2.glb', scale = 12, texture = 'assets/textures/metal_cobre.png', shader = matcap_shader)

        
        rotor = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Rotor/D_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_rotor_mapeado.png')


        eixo = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Eixo/E_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_rotor_eixo.png')


        anel_eixo = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Eixo/E_2.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/cor_anel.png')


        ventoinha_eixo = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Eixo/E_3.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/Plastico.jpg')


        rolD_eixo = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Eixo/E_4.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/prata.jpg')


        rolT_eixo = Entity(parent = self.m_fechado, position = (0,0,0), model = 'assets/Motor_fechado/Eixo/E_5.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/prata.jpg')


        self.MF_dict = {0:tampaT_carcaca, 1:corpo_carcaca, 2:tampaD_carcaca, 3:pes_carcaca, 4:t_dreno,
        5:tampa_terminais, 6:molduraT_terminais, 7:caixa_terminais, 8:terminais, 9:QD_terminais, 
        10:cabos_terminais, 11:painel_terminais, 12:corpo_estator, 13:bobinas_estator, 14:rotor, 15:eixo, 16:anel_eixo, 
        17:ventoinha_eixo, 18:rolD_eixo, 19:rolT_eixo}


    def motor_aberto(self):
        Carcaça = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Carcaça/OA_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        Pes = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Carcaça/OA_2.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        Tampa_dreno = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Carcaça/OA_3.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        Tampa_frontal = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Caixa_terminais/OB_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        Moldura_tampa = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Caixa_terminais/OB_2.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/metal_verde.png')


        Caixa = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Caixa_terminais/OB_3.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_verde.png')


        Terminais = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Caixa_terminais/OB_4.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/metal_cobre.png')


        QD_terminais = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Caixa_terminais/OB_5.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/metal_laranja.png')


        Cabos = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Caixa_terminais/OB_6.obj', scale = 12, shader = basic_lighting_shader)

        
        Estator_corpo = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Estator/OC_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_estator.png')


        Estator_bobinas = Entity(parent = self.m_aberto, position = (0,0,0), rotation_y = 180, model = 'assets/Motor_aberto/Estator/OC_2.glb', scale = 12, texture = 'assets/textures/metal_cobre.png', shader = matcap_shader)

        
        Rotor = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Rotor/OD_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_rotor_mapeado.png')


        Eixo = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Eixo/OE_1.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/metal_rotor_eixo.png')


        Eixo_anel = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Eixo/OE_2.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/cor_anel.png')


        Eixo_ventoinha = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Eixo/OE_3.obj', scale = 12, shader = basic_lighting_shader, collider = 'mesh', texture = 'assets/textures/Plastico.jpg')


        Eixo_rolamento_D = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Eixo/OE_4.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/prata.jpg')


        Eixo_rolamento_T = Entity(parent = self.m_aberto, position = (0,0,0), model = 'assets/Motor_aberto/Eixo/OE_5.obj', scale = 12, shader = basic_lighting_shader, texture = 'assets/textures/prata.jpg')


        self.MA_dict = {1:Carcaça, 2:Pes, 3:Tampa_dreno, 4:Tampa_frontal, 5:Cabos, 6:Estator_corpo, 7:Estator_bobinas, 8:Rotor,
        9:Moldura_tampa, 10:Caixa, 11:Terminais, 12:QD_terminais, 13:Eixo, 14:Eixo_anel, 15:Eixo_ventoinha,
        16:Eixo_rolamento_D, 17:Eixo_rolamento_T}

        pivot = Entity()
        DirectionalLight(parent=pivot, y=0, z=0, shadows=True, rotation=(90, 45, 45))
