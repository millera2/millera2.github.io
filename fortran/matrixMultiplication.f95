program matrixMultiplication

implicit none

! Test program for matrix multiplication

real, dimension(5,5) :: a,b,c
integer :: i,j,k

print *, ""
print *, ""

do i = 1, 5
  do j = 1, 5
    a(i,j)=i*1.0+j*1.0
    b(i,j)=i*j*1.0
  end do
end do

print *, "Matrix A is:"

do i = 1,5
  print "(5F10.2)", a(i,1), a(i,2), a(i,3), a(i,4), a(i,5)
end do

print *, "------"


print *, "Matrix B is:"

do i = 1,5
   print "(5F10.2)", b(i,1), b(i,2), b(i,3), b(i,4), b(i,5)
end do

print *, "------"

do i = 1,5
  do j = 1,5
    do k = 1,5
      c(i,j)=c(i,j)+a(i,k)*b(k, j)
    end do
  end do
end do

print *, "Matrix C = A*B is:"

do i = 1,5
   print "(5F10.2)", c(i,1), c(i,2), c(i,3), c(i,4), c(i,5)
end do


print *, ""
print *, ""
print *, ""

end program


