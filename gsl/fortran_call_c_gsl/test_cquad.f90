module functions_to_integrate

   use iso_c_binding

contains
   function g(x) bind(C)
      real(kind=c_double) :: g
      real(kind=c_double), value :: x
      g = sin(x)/x
   end function g
end module

program test

   use iso_c_binding

   use functions_to_integrate

   interface
      function  my_cquad (f,a,b)  bind(c)
         import
         real (kind=c_double) :: my_cquad

         interface
            function f(x) bind(c)
               import
               real(kind=c_double) :: f
               real(kind=c_double), value :: x 
            end function
         end interface

         real (kind=c_double), value :: a,b
      end function my_cquad
   end interface

   real (kind=c_double) :: y,a,b

   a = 0 ; b = 1
   y = my_cquad(g,a,b)

   print *,y

end program test