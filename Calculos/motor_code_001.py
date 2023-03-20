from math import sqrt

class motor_data:

	def __init__(self, u, pot, ip_in, red, cosphi):
		self.u = u 
		self.pot = pot
		self.ip_in = ip_in
		self.red = red
		self.cosphi = cosphi

	def i_n(self):
		global i_n
		i_n = (self.pot)/(self.u*(self.red/100)*sqrt(3)*self.cosphi)
		# Dividir self.red por 100 porque está em porcentagem 
		print('Corrente nominal: {:.3f}A'.format(i_n))

	def rot_p_m(self):
		global v_eixo, nm
		f = 60 # Frequência da rede - Hz
		poles = int(input('Pares de polos: ')) 
		# Se tiverem dois polos será considerado como 1 par de polos
		v_eixo = (f * 120)/(poles)
		nm = int(input('Velocidade medida no rotor(rpm): ')) 
		print('\nRotações velocidade do eixo(rpm): {:.3f}rpm'.format(v_eixo))

	def i_partida(self):
		i_partida = (i_n * self.ip_in)
		print('Corrente de partida: {:.3f}A'.format(i_partida))		 

	def esc(self):
		# Escorregamento
		esc = ((v_eixo - nm)/(v_eixo))*100
		print('Escorregamento do motor: {:.3f}%'.format(esc))


