
# ==========================================
#       VACUUM CLEANER - TWO ROOMS
# ==========================================

def vacuum_cleaner():
    # Initial state of the two rooms
    room_a = input("Enter status of Room A (Dirty/Clean): ").strip().lower()
    room_b = input("Enter status of Room B (Dirty/Clean): ").strip().lower()

    # Convert input into Boolean values
    rooms = {
        "A": room_a == "dirty",
        "B": room_b == "dirty"
    }

    current_room = "A"

    print("\n================================")
    print("       VACUUM CLEANER AGENT")
    print("================================")

    while True:
        print(f"\nVacuum is currently in Room {current_room}.")

        # Check whether the current room is dirty
        if rooms[current_room]:
            print(f"Room {current_room} is DIRTY.")
            print(f"Cleaning Room {current_room}...")
            rooms[current_room] = False
            print(f"Room {current_room} is now CLEAN.")
        else:
            print(f"Room {current_room} is already CLEAN.")

        # Check whether both rooms are clean
        if not rooms["A"] and not rooms["B"]:
            print("\n✅ Both rooms are clean!")
            print("Vacuum cleaner has finished cleaning.")
            break

        # Move to the other room
        if current_room == "A":
            print("Moving from Room A → Room B")
            current_room = "B"
        else:
            print("Moving from Room B → Room A")
            current_room = "A"


# Run the vacuum cleaner
vacuum_cleaner()
