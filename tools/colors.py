def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def print_colored_block(hex_color):
    try:
        r, g, b = hex_to_rgb(hex_color)
        # colored_block = f"\033[48;2;{r};{g};{b}m{' ' * 10}\033[0m"
        colored_block = f"\033[48;2;{r};{g};{b}m {hex_color} \033[0m"
        print(colored_block)
    except ValueError:
        print(f"Invalid hexadecimal color: {hex_color}")

if __name__ == "__main__":
    hex_color_input = input("Enter a hexadecimal color value (e.g., #FF0000 for red): ")
    print_colored_block(hex_color_input)

