temperaturas = [22, 25, 31, 28, 35, 24]



for temperatura in temperaturas:
    if temperatura > 30:
        print(f"\033[31mALERTA\033[0m: temperatura elevada! {temperatura}°C")
    else:
        print(f"Temperatura registrada: {temperatura}°C")