from PIL import Image
import os

# A list of pixel coordinates to analyze (x, y)
pixels_to_check = [
    (77, 293),
    (154, 264),
    (236, 265),
    (318, 260),
    (401, 265),
    (481, 266),
    (560, 265),
    (639, 266),
    (77, 360),
    (165, 347),
    (237, 343),
    (318, 344),
    (396, 345),
    (478, 345),
    (551, 344),
    (635, 345),
    (83, 417),
    (161, 422),
    (231, 423),
    (315, 424),
    (394, 424),
    (476, 420),
    (558, 423),
    (636, 423),
    (75, 499),
    (159, 500),
    (239, 505),
    (316, 506),
    (404, 504),
    (483, 504),
    (554, 502),
    (636, 504),
    (73, 586),
    (159, 580),
    (241, 578),
    (325, 587),
    (394, 581),
    (475, 584),
    (563, 578),
    (640, 581),
    (84, 657),
    (164, 659),
    (240, 663),
    (321, 660),
    (397, 660),
    (478, 660),
    (555, 664),
    (642, 664),
    (80, 744),
    (161, 747),
    (234, 741),
    (311, 742),
    (400, 741),
    (478, 743),
    (554, 742),
    (636, 741),
    (81, 821),
    (158, 820),
    (238, 826),
    (322, 821),
    (395, 820),
    (476, 821),
    (566, 827),
    (626, 821)
    # Add more pixel coordinates here
]


def get_game_state():
    global game_state
    image_path = os.path.join("newest update", "screenshot.png")
    game_state = []
    if os.path.exists(image_path):
        try:
            # Open the image
            img = Image.open(image_path)
            # Ensure image is in RGB format
            img = img.convert('RGB')

            # Get the color of each pixel in the list
            for x, y in pixels_to_check:
                try:
                    r, g, b = img.getpixel((x, y))
                    if r < 37 and r > 17 and g > 26 and g < 46 and b > 56 and b < 86:
                        game_state.append('b')
                    else:
                        game_state.append('f')
                except IndexError:
                    print(f"Pixel at ({x}, {y}) is out of bounds.")

            # Print the game state in an 8x8 grid
            for i in range(0, len(game_state), 8):
                print(' '.join(game_state[i:i+8]))

        except Exception as e:
            print(f"An error occurred while processing the image: {e}")
            print("Please make sure you have Pillow installed: pip install Pillow")
    else:
        print(f"Error: The file '{image_path}' does not exist.")


peace_slot_1 = [
    (72, 954),
    (102, 954),
    (134, 953),
    (164, 954),
    (190, 954),
    (217, 953),
    (249, 953),
    (72, 976),
    (102, 978),
    (136, 976),
    (165, 977),
    (191, 979),
    (217, 978),
    (250, 979),
    (75, 1004),
    (102, 1004),
    (139, 1002),
    (164, 1002),
    (190, 1002),
    (218, 1003),
    (249, 1003),
    (73, 1026),
    (101, 1030),
    (129, 1031),
    (165, 1032),
    (193, 1032),
    (220, 1033),
    (251, 1033),
    (73, 1051),
    (99, 1057),
    (133, 1054),
    (169, 1058),
    (195, 1058),
    (221, 1058),
    (251, 1059),
    (70, 1085),
    (101, 1085),
    (133, 1080),
    (169, 1081),
    (198, 1084),
    (226, 1084),
    (251, 1084),
    (73, 1116),
    (102, 1116),
    (140, 1114),
    (171, 1114),
    (201, 1114),
    (227, 1114),
    (251, 1114),
    (75, 1142),
    (103, 1142),
    (139, 1142),
    (171, 1142),
    (201, 1142),
    (230, 1142),
    (253, 1144)
]

peace_slot_2 = [
    (260, 939),
    (284, 937),
    (312, 936),
    (337, 934),
    (367, 934),
    (397, 932),
    (434, 932),
    (260, 960),
    (284, 963),
    (306, 963),
    (337, 964),
    (369, 963),
    (396, 964),
    (435, 965),
    (258, 990),
    (282, 990),
    (309, 991),
    (334, 992),
    (368, 993),
    (396, 993),
    (442, 993),
    (259, 1019),
    (278, 1023),
    (305, 1026),
    (329, 1026),
    (364, 1024),
    (397, 1025),
    (442, 1024),
    (262, 1046),
    (280, 1050),
    (306, 1055),
    (334, 1051),
    (367, 1057),
    (398, 1056),
    (436, 1055),
    (260, 1071),
    (282, 1074),
    (309, 1078),
    (335, 1078),
    (364, 1081),
    (402, 1080),
    (436, 1082),
    (264, 1098),
    (288, 1105),
    (319, 1109),
    (337, 1110),
    (365, 1109),
    (403, 1107),
    (437, 1108),
    (264, 1129),
    (289, 1135),
    (316, 1137),
    (344, 1140),
    (368, 1143),
    (404, 1143),
    (439, 1148),
    (260, 1154),
    (288, 1161),
    (316, 1161),
    (344, 1163),
    (369, 1166),
    (398, 1168),
    (436, 1176)
]
peace_slot_3 = [
    (481, 927),
    (511, 924),
    (539, 924),
    (578, 924),
    (610, 921),
    (640, 921),
    (666, 921),
    (481, 950),
    (512, 950),
    (542, 950),
    (579, 950),
    (611, 950),
    (642, 950),
    (670, 950),
    (479, 972),
    (514, 972),
    (545, 972),
    (580, 971),
    (616, 973),
    (642, 974),
    (672, 978),
    (480, 998),
    (513, 996),
    (546, 995),
    (581, 995),
    (617, 997),
    (645, 999),
    (675, 1005),
    (483, 1024),
    (513, 1022),
    (548, 1022),
    (585, 1023),
    (618, 1023),
    (649, 1025),
    (676, 1029),
    (483, 1054),
    (513, 1054),
    (550, 1051),
    (590, 1054),
    (623, 1054),
    (650, 1055),
    (673, 1055),
    (483, 1081),
    (513, 1082),
    (557, 1084),
    (592, 1083),
    (624, 1081),
    (652, 1081),
    (676, 1077),
    (481, 1102),
    (513, 1102),
    (555, 1107),
    (584, 1104),
    (620, 1105),
    (652, 1107),
    (679, 1103),
    (485, 1123),
    (512, 1126),
    (557, 1129),
    (584, 1131),
    (620, 1134),
    (656, 1133),
    (679, 1135),
    (485, 1149),
    (511, 1150),
    (555, 1155),
    (586, 1159),
    (625, 1160),
    (662, 1161),
    (685, 1161),
    (568, 969)
]


def get_peices(peace_locatoins, slot):
    image_path = os.path.join("newest update", "screenshot.png")
    peaces = []
    if os.path.exists(image_path):
        try:
            # Open the image
            img = Image.open(image_path)
            # Ensure image is in RGB format
            img = img.convert('RGB')

            # Get the color of each pixel in the list
            for x, y in peace_locatoins:
                try:
                    r, g, b = img.getpixel((x, y))
                    if r > 43 and r < 67 and g > 75 and g < 95 and b > 135 and b < 160:
                        peaces.append('b')
                    else:
                        peaces.append('f')
                except IndexError:
                    print(f"Pixel at ({x}, {y}) is out of bounds.")

        except Exception as e:
            print(f"An error occurred while processing the image: {e}")
            print("Please make sure you have Pillow installed: pip install Pillow")
    else:
        print(f"Error: The file '{image_path}' does not exist.")
    global slot_1
    global slot_2
    global slot_3
    if slot == 1:
        if peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'no block in slot 1'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'square'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = '3 by 2 horizontal'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = '5 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = '4 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'big corner in the botom right'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'b', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'T'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = '2 by 3 vertical'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = '2 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'top left corner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'big top right corner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'J pointed right'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = '9 by 9 square'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = '4 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'bottem left big corner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'vertical Z'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'upside down T'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'b', 'f', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'L pointed right'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b']:
            slot_1 = '5 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'J pointed left'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'J'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'Z'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'b', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'S'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_1 = 'T pointed left'
        else:
            print(peaces)
            print('unknown slot 1')
            slot_1 = 'unknown'
        print(slot_1)
    if slot == 2:
        if peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'no block in slot 2'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '4 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '2 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'b', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'top left corner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'L pointed left'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'vertical S'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'corner top right'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '3 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '2 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'T pointed right'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'f', 'b', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'S'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'small square'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '2 by 3 vertical'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'big top right corner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'J'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'big bottem left corner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '3 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'T pointed left'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'up side down J'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'f', 'b', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'up side down T'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '4 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '9 by 9 square'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'f', 'f', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = 'five long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_2 = '5 tall line'
        else:
            print(peaces)
            slot_2 = 'unknown slot 2'
        print(slot_2)
    if slot == 3:
        if peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'no block in slot 3'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '4 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '3 by 2 horizontal'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'top left corner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'J pointed right'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '3 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '2 by 3 vertical'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '4 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '2 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'S'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'Z'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '9 by 9 square'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '4 tall line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'upside down J'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'J pointed left'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'small square'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'upside down T'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'vertical Z'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'T'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'big bottem right corrner'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'vertical S'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = '5 long line'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']:
            slot_3 = 'T pointed right'
        elif peaces == ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'f']:
            slot_3 = '5 tall line'
        else:
            print('unknown slot 3')
            print(peaces)
            slot_3 = 'unknown'
        print(slot_3)


def AI():
    global slot_1
    global slot_2
    global slot_3
    global game_state


def exe_interpreter():
    get_game_state()
    get_peices(peace_slot_1, 1)
    get_peices(peace_slot_2, 2)
    get_peices(peace_slot_3, 3)
