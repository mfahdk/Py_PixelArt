import pixart

def draw(lines):
    for j in range(len(lines)):
        string = lines[j]
        for i in range(len(lines[j])):
            i = i - 1
            if string[i] == "0":
                pixart.draw_black_pixel()
                pixart.move(j,i)
            elif string[i] == "1":
                pixart.draw_white_pixel()
                pixart.move(j,i)
            elif string[i] == "2":
                pixart.draw_red_pixel()
                pixart.move(j,i)
            elif string[i] == "3":
                pixart.draw_yellow_pixel()
                pixart.move(j,i)
            elif string[i] == "4":
                pixart.draw_orange_pixel()
                pixart.move(j,i)
            elif string[i] == "5":
                pixart.draw_green_pixel()
                pixart.move(j,i)
            elif string[i] == "6":
                pixart.draw_yellowgreen_pixel()
                pixart.move(j,i)
            elif string[i] == "7":
                pixart.draw_sienna_pixel()
                pixart.move(j,i)
            elif string[i] == "8":
                pixart.draw_tan_pixel()
                pixart.move(j,i)
            elif string[i] == "9":
                pixart.draw_gray_pixel()
                pixart.move(j,i)
            elif string[i] == "A":
                pixart.draw_darkgray_pixel()
                pixart.move(j,i)
            else:
                return False
    return True

def main():
    pixart.initialize()
    drawing01 = "00000000000000000000\n01111111111111111110\n01111111111111111110\n01111111100111111110\n01111111033011111110\n01111110333301111110\n01000000333300000010\n01033333333333333010\n01104333033033340110\n01110433033033401110\n01111043033034011110\n01111043333334011110\n01110433333333401110\n01110433333333401110\n01104334400443340110\n01104440011004440110\n01044001111110044010\n01000111111111100010\n01111111111111111110\n00000000000000000000"
    drawing02 = "0000000000000000000000000\n0111111111111111111111110\n0111111111100011111111110\n0111111110066600111111110\n0111111106656566011111110\n0111111096666666901110110\n0111000965656565690006010\n0110666666666666666665010\n0106556555666555666650110\n0110005101606101665501110\n0111110666666666660011110\n0111111066000666601111110\n0111111106666666011111110\n0111111110066660111111110\n0111111100A8778A011111110\n011111106AA8778AA01111110\n0111110770A8008A601111110\n0111111070A8778A01111111\n0111111070660066011111110\n0111111101001100111111110\n0111111111111111111111110\n0000000000000000000000000"
    drawing03 = "00000000000000000000\n01111111111111111110\n01111112222221111110\n01111122222222211110\n01111177778781111110\n01111787888788811110\n01111787788878881110\n01111778888777711110\n01111118888888111110\n01111177277711111110\n01111777277277711110\n01117777222277771110\n01118872822827881110\n01118882222228881110\n01118822222222881110\n01111122211222111110\n01111777111177711110\n01117777111177771110\n01111111111111111110\n00000000000000000000"
    drawing04 = "00000000000000000000\n09999999999999999990\n09999995555559999990\n09999555555555999990\n09999998080000999990\n09999888088808099990\n09998880888008099990\n09999000088880099990\n09999988888889999990\n09999999111511999990\n09999111511511199990\n09991111555511119990\n09998815155151889990\n09998885555558889990\n09998855555555889990\n09999955599555999990\n09999000999900099990\09990000999900009990\n09999999999999999990\n00000000000000000000"
    drawing = int(input("Which drawing do you want? : "))
    if drawing == 1:
        lines = drawing01.split("\n")
        draw(lines)
    elif drawing == 2:
        lines = drawing02.split("\n")
        draw(lines)
    elif drawing == 3:
        lines = drawing03.split("\n")
        draw(lines)
    elif drawing == 4:
        lines = drawing04.split("\n")
        draw(lines)
main()