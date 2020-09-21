program quadratic

!my first attempt at a simple fortran program

implicit none

real :: a, b, c, disc, x1, x2

print *, "Enter quadratic coefficients a, b, and c:"
print *, "(Seperated by commas)"

read *, a, b, c

disc = b**2-4*a*c



if (disc >0) then
  x1 = (-b+sqrt(disc))/(2*a)
  x2 = (-b-sqrt(disc))/(2*a)

  print *, "Real roots:"
  print *, x1, x2

else if (disc == 0) then
  
  x1 = -b/(2*a)
  print *, "Real root:"
  print *, x1

else
  
  print *, "No real roots"

end if

end program quadratic
