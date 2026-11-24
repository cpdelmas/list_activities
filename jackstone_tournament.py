def get_valid_score(prompt):
  while True:
    try:
      score = int(input(prompt))
      if 0 <= score <= 100:
        return score
      else:
        print("Invalid score. Please enter a score between 0 and 100.")
    except ValueError:
      print("Invalid input. Please enter a valid integer.")


def get_valid_index(prompt, max_index):
  while True:
    try:
      index = int(input(prompt))
      if 0 <= index <= max_index:
        return index
      else:
        print(f"Invalid index. Please enter a number between 0 and {max_index}.")
    except ValueError:
      print("Invalid input. Please enter a valid integer.")

scores = []
print("Please enter 5 initial scores (0-100):")
for i in range(5):
  valid_score = get_valid_score(f"Enter score #{i + 1}: ")
  scores.append(valid_score)

original_scores = scores.copy()

while True:
  print("--- SCORE MANAGEMENT MENU ---")
  print("1. Display Scores")
  print("2. Add Score")
  print("3. Insert Score")
  print("4. Remove Score")
  print("5. Remove Last Score")
  print("6. Search Score")
  print("7. Generate Statistics")
  print("8. Sort Scores")
  print("9. Reverse Scores")
  print("10. Clear Scores")
  print("11. Restore Original Scores")
  print("12. Exit")

  choice = input("Enter your choice (1-12): ").strip()

  if choice == "1":
    print("Current Scores:", scores)

  elif choice == "2":
    new_score = get_valid_score("Enter score to add: ")
    scores.append(new_score)
    print(f"Added {new_score} to the list.")

  elif choice == "3":
    new_score = get_valid_score("Enter score to insert: ")
    idx = get_valid_index(
        f"Enter index to insert at (0 to {len(scores)}): ", len(scores)
    )
    scores.insert(idx, new_score)
    print(f"Inserted {new_score} at index {idx}.")

  elif choice == "4":
    if not scores:
      print("The list is empty. Nothing to remove.")
    else:
      target = get_valid_score("Enter score to remove: ")
      if target in scores:
        scores.remove(target)
        print(f"Removed first occurrence of {target}.")
      else:
        print(f"Score {target} not found in the list.")

  elif choice == "5":
    if not scores:
      print("The list is empty. Nothing to remove.")
    else:
      removed = scores.pop()
      print(f"Removed the last score: {removed}")

  elif choice == "6":
    if not scores:
      print("The list is empty. Nothing to search.")
    else:
      target = get_valid_score("Enter score to search for: ")
      count = scores.count(target)
      if count > 0:
        first_idx = scores.index(target)
        print(
            f"Score {target} appears {count} time(s). First occurrence is at"
            f" index {first_idx}."
        )
      else:
        print(f"Score {target} was not found in the list.")

  elif choice == "7":
    if not scores:
      print("The list is empty. Cannot calculate statistics.")
    else:
      count = len(scores)
      total = sum(scores)
      average = total / count
      highest = max(scores)
      lowest = min(scores)
      print("--- SCORE STATISTICS ---")
      print(f"Count:   {count}")
      print(f"Total:   {total}")
      print(f"Average: {average:.2f}")
      print(f"Highest: {highest}")
      print(f"Lowest:  {lowest}")

  elif choice == "8":
    if not scores:
      print("The list is empty. Nothing to sort.")
    else:
      order = (
          input("Sort in (A)scending or (D)escending order? ").strip().upper()
      )
      if order == "A":

        scores.sort()
        print("Scores sorted in ascending order.")
      elif order == "D":
        scores.sort(reverse=True)
        print("Scores sorted in descending order.")
      else:
        print("Invalid sort option. Please choose 'A' or 'D'.")

  elif choice == "9":
    if not scores:
      print("The list is empty. Nothing to reverse.")
    else:
      scores.reverse()
      print("Scores order reversed.")

  elif choice == "10":
    scores.clear()
    print("All scores have been cleared.")

  elif choice == "11":
    scores = original_scores.copy()
    print("Original scores restored.")

  elif choice == "12":
    print("Exiting program. Goodbye!")
    break

  else:
    print("Invalid menu choice. Please select a number between 1 and 12.")
