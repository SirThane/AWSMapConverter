from PIL import Image, ImageDraw, ImageSequence


def layer(bitmask):
    if isinstance(bitmask, str):
        if bitmask[-2] == "b":
            bitmask = bitmask[::-1]
        bitmask = int(bitmask, 2)
    key = [(x, y) for y in range(4) for x in range(4)]
    return [key[i] for i in range(16) if 2 ** i & bitmask]


palette = {
    "white":    (255, 255, 255),

    "green1":   (168, 240, 80),     # Plain light; Wood light
    "green2":   (104, 232, 56),     # Plain dark
    "green3":   (88,  200, 16),     # Wood dark; GE

    "blue1":    (112, 176, 248),    # Shoal; Reef light
    "blue2":    (56,  120, 248),    # Reef medium; River light
    "blue3":    (88,  104, 248),    # River dark; BM; Sea
    "blue4":    (54,  86,  209),    # CI light
    "blue5":    (20,  43,  135),    # CI dark

    "teal1":    (68,  172, 163),    # TG light
    "teal2":    (10,  89,  82),     # TG dark

    "grey1":    (166, 182, 153),    # JS
    "grey2":    (184, 176, 168),    # Road; Bridge; Silo
    "grey3":    (129, 127, 128),    # GS light
    "grey4":    (86,  92,  114),    # GS dark

    "red1":     (176, 144, 136),    # Pipe; Pipe Seam; Broken Pipe Seam
    "red2":     (248, 72,  48),     # OS
    "red3":     (208, 70,  93),     # RF light
    "red4":     (119, 11,  35),     # RF dark

    "pink":     (255, 102, 204),    # PC

    "purple1":  (164, 70,  210),    # PL light
    "purple2":  (110, 25,  153),    # PL dark
    "purple3":  (96,  72,  160),    # BH light
    "purple4":  (79,  48,  112),    # BH dark

    "yellow":   (240, 240, 8),      # YC

    "orange1":  (248, 232, 144),    # Mountain light; Reef light
    "orange2":  (207, 179, 158),    # BD light
    "orange3":  (252, 163, 57),     # AB
    "orange4":  (208, 128, 48),     # Mountain medium; Reef dark
    "orange5":  (147, 82,  50),     # BD dark

    "brown1":   (152, 104, 48),     # Mountain dark
    "brown2":   (104, 80,  56),     # Borders
}

spec = {
    "plain": [
        {
            "xy":   layer("1111110111110111b0"),
            "fill": palette["green1"]
        },
        {
            "xy":   layer("0000001000001000b0"),
            "fill": palette["green2"]
        }
    ],
    "mountain": [
        {
            "xy":   layer("1111100100000000b0"),
            "fill": palette["green1"]
        },
        {
            "xy":   layer("0000010011001000b0"),
            "fill": palette["orange1"]
        },
        {
            "xy":   layer("0000000000000100b0"),
            "fill": palette["orange4"]
        },
        {
            "xy":   layer("0000001000110011b0"),
            "fill": palette["brown1"]
        }
    ],
    "wood": [
        {
            "xy":   layer("1001000000001001b0"),
            "fill": palette["green1"]
        },
        {
            "xy":   layer("0110111011000000b0"),
            "fill": palette["green2"]
        },
        {
            "xy":   layer("0000000100110110b0"),
            "fill": palette["green3"]
        }
    ],
    "river": [
        {
            "xy":   layer("1111001111111000b0"),
            "fill": palette["blue2"]
        },
        {
            "xy":   layer("0000110000000111b0"),
            "fill": palette["blue3"]
        }
    ],
    "road": [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": palette["grey2"]
        }
    ],
    "sea": [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": palette["blue3"]
        }
    ],
    "shoal": [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": palette["blue1"]
        }
    ],
    "reef": [
        {
            "xy":   layer("1000001000000000b0"),
            "fill": palette["orange1"]
        },
        {
            "xy":   layer("0000100000100000b0"),
            "fill": palette["orange4"]
        },
        {
            "xy":   layer("0000010010010010b0"),
            "fill": palette["blue1"]
        },
        {
            "xy":   layer("0000000001000001b0"),
            "fill": palette["blue2"]
        },
        {
            "xy":   layer("0111000100001100b0"),
            "fill": palette["blue3"]
        },
    ],
    "pipe": [
        {
            "xy":   layer("1111111111111111b0"),
            "fill": palette["red1"]
        }
    ],
    "silo": [
        {
            "xy":   layer("1010101010100000b0"),
            "fill": palette["white"]
        },
        {
            "xy":   layer("0100010001000000b0"),
            "fill": palette["grey2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "osprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["red2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "bmprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["blue3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "geprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["green3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "ycprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["yellow"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "bhprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["purple3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["purple4"]
        }
    ],
    "rfprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["red2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["red4"]
        }
    ],
    "gsprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["grey3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["grey4"]
        }
    ],
    "bdprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["orange2"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["orange5"]
        }
    ],
    "abprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["orange3"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "jsprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["grey1"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "ciprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["blue4"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["blue5"]
        }
    ],
    "pcprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["pink"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["brown2"]
        }
    ],
    "tgprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["teal1"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["teal2"]
        }
    ],
    "plprop": [
        {
            "xy":   layer("1110111011100000b0"),
            "fill": palette["purple1"]
        },
        {
            "xy":   layer("0001000100011111b0"),
            "fill": palette["purple2"]
        }
    ],
}


im = Image.new("RGBA", (4, 4))
draw = ImageDraw.Draw(im)
for layer in spec["bmprop"]:
    draw.point(**layer)
im.save("test.png")





# im = Image.open("test.png", mode="r")
# print(dir(im))