from typing import List, Tuple, Union

def calculate_grade(assignment_scores: List[Union[int, float]], mid_score: Union[int, float], final_score: Union[int, float]) -> Tuple[float, str]:
  
  def weighted_average() -> float:
    assignment_score = sum(assignment_scores) / len(assignment_scores)
    return (assignment_score * 0.4) + (mid_score * 0.3) + (final_score * 0.3)
  
  def determine_grade(average: float) -> str:
    return 'A' if average >= 90 else 'B' if 90 > average >= 80 else 'C' if 80 > average >= 70 else 'D'
  
  average = weighted_average()
  grade = determine_grade(average)

  return average, grade

def main():
  final_average, final_grade = calculate_grade([92, 80, 50], 95, 77)
  print(f"Final average = {final_average:.2f}, Final grade = {final_grade}")

if __name__ == "__main__":
  main()