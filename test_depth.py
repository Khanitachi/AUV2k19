from motion import movement

m = movement.Movement()

def main():
    while True:
        try:
            m.hp_control()
        except KeyboardInterrupt:
            print('Oh No!')
            m.hold()
            break

if __name__ == "__main__":
    main()