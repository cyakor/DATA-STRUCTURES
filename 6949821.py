#Username is 'cyakor'
#Civil Engineering 2
'Yakor Calvin'
#'Index Number '6949821''
# www.github.com/cyakor

w=10                          #Load intensity
l=12                          #Length of beam
x_1=0                         #X equals 0
x_2=l                         #X equals length of beam
#question a

bending_moment1=(w*(((-6)*(x_1**2)+(6*l*x_1))-(l*l)))/(12)   #bending moment at x equals 0
bending_moment2=(w*(((-6)*(x_2**2)+(6*l*x_2))-(l*l)))/(12)   #bending moment at x equals l
print(bending_moment1)
print(bending_moment2)

shear_force1=w*(l/2-x_1)       #shear force at x equals 0
shear_force2=w*(l/2-x_2)       #shear force at x equals l
print(shear_force1)
print(shear_force2)

#question b
import numpy as np
discriminant=np.sqrt(((72)**2)-(4*6*144))
root1=((72+np.sqrt((discriminant)))/(2*6))      #First answer of root
root2=((72-np.sqrt((discriminant)))/(2*6))      #Second answer of root

#question c              The point at which the shear force will be zero
xwhenshearequals0=l/2


#question d
d=np.linspace(0,12,1200)
bendingmomentateverystep=(w*((-6*(d**2)+(6*l*d)-(l**2))))/12   


#question e
shearateverystep=(((w*l/2)-(w*d)))       #shear force at every point
          

#question f           Points where the absolute values of bending moment is minimum
ab_bending_moment_min_1=2.53211
ab_bending_moment_min_2=9.46789

#question g             Errors between the estimated points of contra-flexure
discriminant_g=np.sqrt((720**2)-(4*-60*-144))
error_1=((-720+discriminant_g)/(2*-60))
error_2=((-720-discriminant_g)/(2*-60))


#question h               Bending moment is minimum at the supports
bending_moment_min_1=0      #Minimum bending moment is -120
bending_moment_min_2=12

bending_moment_max_at_x_1=6.005      #Maximum bending moment is 59.9999
bending_moment_max_at_x_2=5.995
