class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

  def set_width(self,width):
    if isinstance(self,Square):
      self.set_side(width)
    else:  
      self.width = width

  def set_height(self,height):
    if isinstance(self,Square):
      self.set_side(height)
    else:  
      self.height = height
  
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ''  
    for i in range(self.height):
      for j in range(self.width):
        picture += '*'
      picture += '\n'
    return picture

  def get_amount_inside(self,shape):
    inner_width = shape.width
    inner_height = shape.height
    outer_width = self.width
    outer_height = self.height
    return self._get_amount_inside(outer_width,outer_height,inner_width,inner_height)

  def get_amount_inside_with_rotation(self,shape):
    inner_width = shape.width
    inner_height = shape.height
    outer_width = self.width
    rotate_outer_width = self.height
    rotate_outer_height = self.width
    outer_height = self.height
    result = self._get_amount_inside(outer_width,outer_height,inner_width,inner_height) + self._get_amount_inside((outer_height % inner_height),outer_width,inner_width,inner_height) + self._get_amount_inside(outer_height,outer_width % inner_width,inner_width,inner_height)
    result_rotate = self._get_amount_inside(rotate_outer_width,rotate_outer_height,inner_width,inner_height) + self._get_amount_inside((rotate_outer_height % inner_height),rotate_outer_width,inner_width,inner_height) + self._get_amount_inside(rotate_outer_height,rotate_outer_width % inner_width,inner_width,inner_height)
    
    return max([result,result_rotate])
    
  def _get_amount_inside(self,outer_width,outer_height,inner_width,inner_height,n=0):
    width = outer_width
    if outer_width < inner_width or outer_height < inner_height:
      return n 
    else:
      while width >= inner_width:
        n += 1
        width -= inner_width
      n += self._get_amount_inside(outer_width,(outer_height - inner_height),inner_width,inner_height)
      return n 


class Square(Rectangle):
  def __init__(self,side):
    self.side = side
    self.width = self.side
    self.height = self.side

  def __str__(self):
    return f'Square(side={self.side})'

  def set_side(self,side):
    self.side = side
    self.width = side
    self.height = side

    