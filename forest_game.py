import numpy as np

class Forest:
    def __init__(self, lattice_lenght, interaction ,p_death, p_birth, max_size, empty = True):
        self.L = lattice_lenght
        self.y = interaction
        self.pd = p_death
        self.pb = p_birth
        self.S_max = max_size
        
        #construction
        if empty:
            self.forest = np.zeros((self.L+2,self.L+2))
        else:
            self.forest = np.random.rand(self.L+2,self.L+2)*self.S_max
        #counter
        self.n_birth = 0
        self.n_death = 0
        self.n_growth = 0
        
   
    def step(self):
        i,j  = np.random.randint(low =1, high = self.L+1 , size =2)
        
        if self.forest[i][j]==0:
            self.birth(i,j)
        else:
            self.growth(i,j)
            
    def ReLu(self,x):
        if x>=0:
            return x
        else:
            return 0
            
    def birth(self,i,j):
        if np.random.rand() < self.pb:
            self.forest[i][j] = 0.1
            self.n_birth += 1

    def growth(self,i,j):
        if np.random.rand() < self.pd:
            self.death(i,j)
            self.n_death += 1
        else:
            ds = self.increment(i,j)
            self.forest[i][j] += ds
            self.n_growth += 1
            if self.forest[i][j] > self.S_max:
                self.death(i,j)
       
        #zeroing the boundaries
        for B in range(self.L+1):
            self.forest[0][B] = 0
            self.forest[self.L+1][B] = 0
            self.forest[B][0] = 0
            self.forest[B][self.L+1] = 0
    
    def increment(self,i,j):
        #somma dei size dei primi vicini
        S = 0
        for a in [i-1,i,i+1]:
            for b in [j-1,j,j+1]:
                S += self.forest[a,b]
        S-=self.forest[i,j]
        
        return self.ReLu( 1- (self.y/8)*S )
        
        
    def death(self,i,j):
        
        to_remove = np.random.rand()*self.forest[i][j]
        
        for a in [i-1,i,i+1]:
            for b in [j-1,j,j+1]:
                self.forest[a,b] = self.ReLu( self.forest[a,b] - to_remove/8)
        
        self.forest[i][j] = 0
    
    def get_num(self):
        print('birth events :',self.n_birth) 
        print('death events :',self.n_death) 
        print('growth events :',self.n_growth)
        
        
        
        
        
        