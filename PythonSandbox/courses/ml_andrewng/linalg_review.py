"""
Machine Learning Andrew Ng - Linear Algebra Review

note: unlike Matlab, where * implies vector multiplication,
* in python performs scalar multiplication, and @ performs vector.
"""
import numpy as np

def matrices_and_vectors():
    A = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9], 
         [10, 11, 12]]
    print(A)
    
    B = np.array(A)
    print(B)
    
    print("B dimensions:", B.shape)
    print("B^T:\n", B.transpose())

def addition_and_scalar_multiplication():
    A = np.array(
        [[1, 2, 4], 
        [5, 3, 2]])
    B = np.array(
        [[1, 3, 4],
         [1, 1, 1]])
    s = 2
    
    add_AB = np.add(A,B)
    print("add_AB:\n", add_AB)
    print("equal?:\n", add_AB == (A+B))
    ans = np.array_equal(add_AB, A+B) # wholistic single answer True or False; True only if all elements match
    print("entire array equal?:\n", ans)
    
    print("sub_AB:\n", A-B)
    print("mult_As:\n", A*s) # * means scalar mult
    print("div_As:\n", A/s)
    print("add_As:\n", A+s)

def matrix_vector_multiplication():
    A = np.array([[1,3],[4,0],[2,1]])
    B = np.array([[1],[5]])
    print("A@B:\n", A@B) # @ means vector mult
    
    C = np.array([[1,2,1,5],[0,3,0,4],[-1,-2,0,0]])
    D = np.array([[1],[3],[2],[1]])
    print("C@D:\n", C@D)
    
    E = np.array([[1,2,3],[4,5,6],[7,8,9]])
    v = np.array([[1]]*3) # shortcut for [[1], [1], [1]]
    Ev = E@v
    print("Ev:\n", Ev)

def matrix_multiplication_properties():
    A = np.array([[1,2],[4,5]])
    I = np.identity(2)
    print("identity:\n", I)
    
    IA = I@A
    print("IA:\n", IA)
    print(np.array_equal(IA,A))

def inverse_and_transpose():
    A = np.array([[3,4],[5,16]])
    Ainverse = np.linalg.inv(A)
    print("Ainverse:\n", Ainverse)
    Atranspose = np.transpose(A)
    print("Atranspose:\n", Atranspose)

def quiz():
#     u = np.array([[8],[1],[4]])
#     print(np.transpose(u))

    #q4
    u = np.array([[4],[-4],[-3]])
    v = np.array([[4],[2],[4]])
    print(np.transpose(u)@v)
    
    

def main():
    #matrices_and_vectors()
    #addition_and_scalar_multiplication()
    #matrix_vector_multiplication()
    #matrix_multiplication_properties()
    #inverse_and_transpose()
    quiz()
    pass

if __name__ == "__main__":
    main()