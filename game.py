import numpy as np

def test1(d,i,j):
	x=1
	y=2
	if((d[i][j]==x)and(d[i-1][j+1]==x)and(d[i-2][j+2]==x)and(d[i-3][j+3]==x)):
		return 1
	elif((d[i][j]==y)and(d[i-1][j+1]==y)and(d[i-2][j+2]==y)and(d[i-3][j+3]==y)):
		return 2
	else:
		return 0

def test2(d,i,j):
	x=1
	y=2
	if((d[i][j]==x)and(d[i+1][j+1]==x)and(d[i+2][j+2]==x)and(d[i+3][j+3]==x)):
		return 1
	elif((d[i][j]==y)and(d[i+1][j+1]==y)and(d[i+2][j+2]==y)and(d[i+3][j+3]==y)):
		return 2
	else:
		return 0		

def test4(d,i,j):
	x=1
	y=2
	if((d[i][j]==x)and(d[i+1][j]==x)and(d[i+2][j]==x)and(d[i+3][j]==x)):
		return 1
	elif((d[i][j]==y)and(d[i+1][j]==y)and(d[i+2][j]==y)and(d[i+3][j]==y)):
		return 2
	else:
		return 0

def test3(d,i,j):
	x=1
	y=2
	if((d[i][j]==x)and(d[i][j+1]==x)and(d[i][j+2]==x)and(d[i][j+3]==x)):
		return 1
	elif((d[i][j]==y)and(d[i][j+1]==y)and(d[i][j+2]==y)and(d[i][j+3]==y)):
		return 2
	else:
		return 0		

def available(d,x):
	if(x==10):
		return -2
	else:	

		i=5
		while (i>=0):
			if (d[i][x]==0.0):
				return i
			else:
				i=i-1
		return -1


class the_game:
	d = np.zeros((6,7))	
	game_end=0

	def __init__(self):
		print("game created")
		self.reset()


	def reset(self):
		for i in range(6):
			for j in range(7):
				self.d[i][j]=0

	def check_win(self):
		x=1
		y=2
		t=0
		for i in range(3,6):
			for j in range(0,4):
				
				t=test1(self.d,i,j)
				if(t!=0):
					return t
		for i in range(0,3):
			for j in range(0,4):
				
				t=test2(self.d,i,j)
				if(t!=0):
					return t			
		for i in range(0,6):
			for j in range(0,4):
				
				t=test3(self.d,i,j)
				if(t!=0):
					return t

		for i in range(0,3):
			for j in range(0,7):
				
				t=test4(self.d,i,j)
				if(t!=0):
					return t			

		return 0			
	
	

	def play(self,p,x):
		t=available(self.d,x)
		
		if(x in range(7)):
			
			if(p==1):
				self.d[t][x]=1
			if(p==2):
				self.d[t][x]=2

			return t	
		if(x==10):
			self.reset()
		return t	

	def get_d(self):
		return self.d
	def get_game_end(self):
		return self.game_end

					
				


