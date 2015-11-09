%hide
%auto
var('x,y,t,s')                                                                      
@interact(layout=dict(top=[['F1','u'], ['F2','v']],  
          bottom=[['a', 'b'], ['xx'],['yy']]))
def _(F1=input_box(default=-y, width=30),
      F2=input_box(default=x, width=30),
      u=input_box(default = cos(t), width=30),
      v=input_box(default = sin(t), width=30),
      a=input_box(default = 0, width=10),
      b=input_box(default = 2*pi, width=10),
      xx = range_slider(-5, 5, 1, default=(-2,2), label='x Range'),
      yy = range_slider(-5, 5, 1, default=(-2,2), label='y Range')):
  F1(x,y) = F1
  F2(x,y) = F2
  u(t) = u
  v(y) = v
  bigT = vector( (derivative(u(t),t).simplify_trig() , 
                  derivative(v(t),t).simplify_trig() ))
  bigF = vector( (F1(x = u(t), y = v(t)).simplify_trig(),  
                  F2(x = u(t), y = v(t)).simplify_trig() ) )
  print 'F = < %s, %s > ' % ( str(F1(x,y)), str(F2(x,y)))
  print 'r(t) = < %s, %s > ' % ( str(u(t)), str(v(t)) )
  print 'substituting gives: '
  print 'F = %s,\nT = %s' % ( str(bigF), str(bigT) )
  integrand = bigF.dot_product(bigT).simplify_trig().simplify()
  print 'F dot T = %s' % integrand
  print 'integrating from %s to %s gives...' % (str(a), str(b))
  line_integral = integral(integrand,t,a,b)
  html('<h2 align=center>Line Integral = %s</h2>'%str(line_integral))
  G = plot_vector_field((F1(x,y),F2(x,y)),(x,xx[0],xx[1]),(y,yy[0],yy[1]))
  G += parametric_plot([u(t),v(t)],(t,a,b),thickness='5',color='yellow')
  show(G) 
