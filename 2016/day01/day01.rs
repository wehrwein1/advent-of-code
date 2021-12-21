// https://adventofcode.com/2016/day/1
// First time doing something non-trivial in Rust (won't be pretty)

use std::collections::HashSet;
use std::option::Option;

mod geometry; // include geometry.rs 
type Point = geometry::Point<i32>;
type Vector = geometry::Vector;

pub fn main() {
  println!("part 1: blocks away: {}", blocks_away(include_str!("../input/01_INPUT.txt")).0);
  println!("part 2: first location visited twice blocks away: {}", blocks_away(include_str!("../input/01_INPUT.txt")).1);
}

#[derive(Debug, Copy, Clone, PartialEq)]
enum Direction {
  North = 0,
  East,
  South,
  West,
}

impl Direction {
  const DIRECTIONS: [Direction; 4] = [
    Direction::North,
    Direction::East,
    Direction::South,
    Direction::West,
  ];

  fn to_vector(&self) -> Vector {
    let origin = Point { x: 0, y : 0};
    match *self {
      Direction::North => Vector{ start: origin, end: Point{ x: 0,  y:  1}}, // up
      Direction::South => Vector{ start: origin, end: Point{ x: 0,  y: -1}}, // down
      Direction::East =>  Vector{ start: origin, end: Point{ x: 1,  y:  0}},
      Direction::West =>  Vector{ start: origin, end: Point{ x: -1, y:  0}},
    }
  }

  fn turn_left(self) -> Direction {
    let len = Direction::DIRECTIONS.len();
    return Direction::DIRECTIONS[(self as usize + len - 1) % len].clone();
  }

  fn turn_right(self) -> Direction {
    let len = Direction::DIRECTIONS.len();
    return Direction::DIRECTIONS[(self as usize + len + 1) % len].clone();
  }
}

fn blocks_away(instructions: &str) -> (i32, i32) {
  let mut last_ended_at: Point = Point{ x: 0, y: 0 };
  let mut facing_direction: Direction = Direction::North;
  let mut visited_points: HashSet<Point> = HashSet::new();
  let mut first_point_visited_twice: Option<Point> = None;
  let instruction = instructions.split(", ");
  // println!("Start facing {:?}", facing_direction);
  for (i, token) in instruction.enumerate() {
    let (turnchar, distancechars) = token.split_at(1);
    // println!(" {} {}: facing {:?} pos {}", turnchar, distancechars, facing_direction, pos);
    let initial_pos = last_ended_at;
    let initial_facing = facing_direction;
    // turn
    match turnchar {
      "L" => facing_direction = facing_direction.turn_left(),
      "R" => facing_direction = facing_direction.turn_right(),
      _ => {
        panic!("{}", format!("unknown Turn: '{}'", turnchar));
      }
    }
    // move / check path points
    let distance: i32 = distancechars.parse::<i32>().unwrap();
    let walked_path = facing_direction.to_vector().times_scalar(distance).project_from(initial_pos);
    let walked_points = &walked_path.to_points();
    // println!(" about to walk from {:?} to {:?}: pts -> {:?}", pos, walked_path.end, walked_points);
    for walked_point in walked_points {
      if first_point_visited_twice.is_none() && (last_ended_at != *walked_point) && visited_points.contains(walked_point) {
        println!("!! visited before {:?}", walked_point);
        first_point_visited_twice = Some(*walked_point);
      }
      visited_points.insert(*walked_point);
    }
    last_ended_at = walked_path.end;
    println!("{:03} {} facing {:?} -> {}{} ({})-> {} facing {:?}", i, initial_pos, initial_facing, turnchar, distance, walked_points.len(), last_ended_at, facing_direction);
  }
  return (manhattan_distance(last_ended_at), manhattan_distance(first_point_visited_twice.unwrap_or_default()));
}

fn manhattan_distance(pos: Point) -> i32 {
  return pos.x.abs() + pos.y.abs();
}

#[cfg(test)]
mod day01_tests {
  use super::*;

  #[test]
  fn test_day_part1() {
    assert_eq!(1, blocks_away("R1").0);
    assert_eq!(5, blocks_away("R2, L3").0);
    assert_eq!(2, blocks_away("R2, R2, R2").0);
    assert_eq!(12, blocks_away("R5, L5, R5, R3").0);
  }

  #[test]
  fn test_direction() {
    assert_eq!(Direction::North.turn_left(), Direction::West);
    assert_eq!(Direction::North.turn_right(), Direction::East);
    assert_eq!(Direction::West.turn_left(), Direction::South)
  }

  #[test]
  fn test_day_part2() {
    assert_eq!(4, blocks_away("R8, R4, R4, R8").1);
  }
}
