use std::fmt;

#[derive(Eq, PartialEq, Hash, Debug, Default, Copy, Clone)]
pub struct Point<T> {
  pub x: T,
  pub y: T,
}

// 2D vector, not to be confused with Vec<>
#[derive(Debug, Eq, PartialEq)]
pub struct Vector {
  pub start: Point<i32>,
  pub end: Point<i32>,
}

impl fmt::Display for Point<i32> {
  fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
    write!(f, "({},{})", self.x, self.y)
  }
}

impl Vector {

  // pub fn from_origin_to(end_x: i32, end_y: i32) -> Vector {
  //   return Vector{ start: Point{ x: 0, y: 0 }, end: Point{ x: end_x, y: end_y} }
  // }

  pub fn to_points(&self) -> Vec<Point<i32>> {
    let mut points: Vec<Point<i32>> = Vec::new();  
    if self.is_single_point() {
      points.push(Point { x: self.start.x, y : self.start.y});
      return points;
    }
    let (mut x1, mut y1, mut x2, mut y2) = (self.start.x, self.start.y, self.end.x, self.end.y);
    if self.is_horizontal_line() {
      let y = y1;      // vary x, y constant
      if x1 > x2 {     // enforce x2 > x1 relation for loop increment
        let temp = x1;
        x1 = x2;
        x2 = temp;
      }
      for x in x1..x2+1 {
        points.push(Point{ x: x, y: y})
      }
      return points
    }
    if self.is_vertical_line() {
      let x = x1;      // vary y, x constant
      if y1 > y2 { // enforce y2 > y1 relation for loop increment
        let temp = y1;
        y1 = y2;
        y2 = temp;
      }
      for y in y1..y2+1 {
        points.push(Point{ x: x, y: y})
      }
      return points
    }
    if self.is_diagonal_line() {
      panic!("{}", format!("diagonal handling not implemented: '{:?}'", self));  
    }
    panic!("{}", format!("unhandled case: '{:?}'", self));
  }

  pub fn times_scalar(&self, scalar: i32) -> Vector {
    return Vector{
      start: Point{ x: self.start.x * scalar, y: self.start.y * scalar },
      end:   Point{ x: self.end.x   * scalar, y: self.end.y   * scalar }
    }
  }

  pub fn project_from(&self, origin: Point<i32>) -> Vector {
    return Vector{
      start: Point{ x: self.start.x + origin.x, y: self.start.y + origin.y },
      end:   Point{ x: self.end.x   + origin.x, y: self.end.y   + origin.y }
    }
  }

  fn is_horizontal_line(&self) -> bool {
    return !self.is_single_point() && (self.start.y == self.end.y);
  }
  fn is_vertical_line(&self) -> bool {
    return !self.is_single_point() && (self.start.x == self.end.x);
  }
  fn is_single_point(&self) -> bool {
    return (self.start.x == self.end.x) && (self.start.y == self.end.y);
  }
  fn is_diagonal_line(&self) -> bool {
    return (self.start.x != self.end.x) && (self.start.y != self.end.y);
  }
}

#[cfg(test)]
mod geometry_tests {
  use super::*;

  fn single_point_vector()    -> Vector{ return Vector{ start: Point{ x: 4, y: 5 }, end: Point{ x: 4, y: 5 }} }
  fn horizontal_line_vector() -> Vector{ return Vector{ start: Point{ x: 0, y: 3 }, end: Point{ x: 2, y: 3 }} } // same y
  fn vertical_line_vector()   -> Vector{ return Vector{ start: Point{ x: 3, y: 0 }, end: Point{ x: 3, y: 2 }} } // same x
  fn diagonal_line_vector()   -> Vector{ return Vector{ start: Point{ x: 0, y: 0 }, end: Point{ x: 1, y: 1 }} }

  #[test]
  fn test_vector_is_single_point() {
    assert_eq!(true,     single_point_vector().is_single_point());
    assert_eq!(false, horizontal_line_vector().is_single_point());
    assert_eq!(false,   vertical_line_vector().is_single_point());
    assert_eq!(false,   diagonal_line_vector().is_single_point());
  }

  #[test]
  fn test_vector_is_horizontal_line() {
    assert_eq!(false,   single_point_vector().is_horizontal_line());
    assert_eq!(true, horizontal_line_vector().is_horizontal_line());
    assert_eq!(false,  vertical_line_vector().is_horizontal_line());
    assert_eq!(false,  diagonal_line_vector().is_horizontal_line());
  }

  #[test]
  fn test_vector_is_vertical_line() {
    assert_eq!(false,    single_point_vector().is_vertical_line());
    assert_eq!(false, horizontal_line_vector().is_vertical_line());
    assert_eq!(true,    vertical_line_vector().is_vertical_line());
    assert_eq!(false,   diagonal_line_vector().is_vertical_line());
  }

  #[test]
  fn test_vector_is_diagonal_line() {
    assert_eq!(false,    single_point_vector().is_diagonal_line());
    assert_eq!(false, horizontal_line_vector().is_diagonal_line());
    assert_eq!(false,   vertical_line_vector().is_diagonal_line());
    assert_eq!(true,    diagonal_line_vector().is_diagonal_line());
  }

  #[test]
  fn test_to_points() {
    assert_eq!(vec!(Point{ x: 4, y: 5}), single_point_vector().to_points()); 
    assert_eq!(vec!(Point{ x: 0, y: 3}, Point{ x: 1, y: 3}, Point{ x: 2, y: 3}), horizontal_line_vector().to_points());
    assert_eq!(vec!(Point{ x: 3, y: 0}, Point{ x: 3, y: 1}, Point{ x: 3, y: 2}), vertical_line_vector().to_points());
  }

  #[test]
  fn test_times_scalar() {
    assert_eq!(Vector{ start: Point{ x: 0, y: 0 }, end: Point{ x: 15, y: 0}}, 
               Vector{ start: Point{ x: 0, y: 0 }, end: Point{ x: 1,  y: 0}}.times_scalar(15))
  }

  #[test]
  fn test_project_from() {
    assert_eq!(Vector{ start: Point{ x: 3, y: 3 }, end: Point{ x: 4, y: 3 }}, 
               Vector{ start: Point{ x: 0, y: 0 }, end: Point{ x: 1, y: 0 }}.project_from(Point { x: 3, y: 3}))
  }

  // #[test]
  // fn test_from_origin_to() {
  //   assert_eq!(Vector{ start: Point{ x: 0, y: 0 }, end: Point{ x: 5, y: 4 }},
  //              Vector::from_origin_to(5, 4))
  // }
}
