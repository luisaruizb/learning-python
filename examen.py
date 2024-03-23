def example():
    ans = 0 
    operar = False

    while operar:
        try: 
            numero = float(input("numero"))
            ans += numero

            if numero == 0:
                operar = False
            else: 
                print(ans)

        except ValueError:
            print("error")

    print(ans)

example()


