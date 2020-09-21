program randomWalks

implicit none

real :: randomWalkDistance, sumDistance

integer, parameter :: steps = 5000, repetitions = 1000
integer :: i,j

do j = 1, repetitions
  do i = 1,steps
    sumDistance = sumDistance+randomWalkDistance(steps)
  end do
end do
print *, sumDistance/(repetitions*repetitions)

end program randomWalks

function randomWalkDistance(steps)

implicit none

real :: r,x,y, randomWalkDistance
integer :: i,steps

do i=1,steps
  call random_number(r)
  if (r < .25) then
    x = x+1
  else if (r >= .25 .and. r<.5) then
    y = y+1
  else if (r >= .5 .and. r<.75) then
    x = x-1
  else 
    y = y-1
  end if
end do

randomWalkDistance = sqrt(x**2+y**2)

end function randomWalkDistance
