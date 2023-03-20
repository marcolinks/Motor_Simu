from motor_code_001 import motor_data

print('\nMotor Trifásico: 220/380/440 V\n')
motor_1 = motor_data(float(input('Tensão(V): ')), float(input('Potência(W): ')), float(input('Relação de corrente Ip/In(A): ')), float(input('Rendimento(%): ')), float(input('Fator de Potência(Cosphi): ')))

motor_1.rot_p_m()
# Velocidade no eixo
motor_1.esc()
# Escorregamento do motor
motor_1.i_n()		
# Corrente nominal
motor_1.i_partida()
# Corrente de partida
