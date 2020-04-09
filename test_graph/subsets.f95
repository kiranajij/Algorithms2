program subsets_generator
    
    implicit none
    integer :: n, i
    integer, dimension(20):: arr, targ
    logical:: subsets, r

    print *, "Enter number of elements"
    read *, n

    print *, "Enter elements of the array"
    read *, (arr(i), i=1, n)

    r = subsets(arr, n, targ, 1, 1)

end program subsets_generator

recursive function subsets(arr, len, targ, i, j) result(r)
    integer, dimension(20):: arr, targ
    integer, intent(in)   :: len, i, j
    logical               :: r,   s, t

    if ( i == len+1 ) then
        call process_solution(targ, j-1)
        return
    end if

    s = subsets(arr, len, targ, i+1, j)
    targ(j) = arr(i)
    t = subsets(arr, len, targ, i+1, j+1)

    r = .true.
    return

end function subsets

subroutine process_solution(arr, len)
    integer, dimension(20):: arr
    integer :: len

    ! print '("[", $)'
    print '(I3, $)', (arr(i), i=1, len)
    ! print '("]")'
end subroutine process_solution