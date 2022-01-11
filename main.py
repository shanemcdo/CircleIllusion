import os
from CircleIllusion import CircleIllusion

def main():
    os.environ["SDL_VIDEO_WINDOW_POS"] = "15,45"
    CircleIllusion.print_controls()
    c = CircleIllusion(600, 600)
    c.run()

if __name__ == "__main__":
    main()
