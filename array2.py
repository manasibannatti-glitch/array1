
def main():
    scores = [78, 85, 90, 66, 85]
    total = sum(scores)
    average = total / len(scores)
    
    print(f"scores: {scores}")
    print(f"sum: {total}")
    print(f"average: {average}")
    print("\n=== local branch output (max and min) ===")
    print(f"maximum: {max(scores)}")
    print(f"minimum: {min(scores)}")

if __name__ == "__main__":
    main()
